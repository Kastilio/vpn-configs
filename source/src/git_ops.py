import subprocess
import os
import time
from src.config import GITHUBMIRROR_DIR, README_PATH, GIT_ROOT
from src.logger import log, offset

# -------------------- GIT --------------------

MAX_PUSH_ATTEMPTS = 3
RETRY_DELAY_SEC = 5


def _run(args, check=True):
    """Обёртка над subprocess.run с логированием команды."""
    log(f"$ {' '.join(args)}")
    return subprocess.run(args, check=check, cwd=GIT_ROOT)


def _has_staged_changes() -> bool:
    """True, если есть что коммитить."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=GIT_ROOT,
    )
    # returncode == 0 → нет изменений; != 0 → есть
    return result.returncode != 0


def _pull_rebase() -> bool:
    """
    Делает git fetch + git pull --rebase origin main.
    Возвращает True при успехе, False при конфликте (с abort'ом).
    """
    try:
        _run(["git", "fetch", "origin", "main"])
        _run(["git", "pull", "--rebase", "origin", "main"])
        return True
    except subprocess.CalledProcessError as e:
        log(f"⚠️ pull --rebase не удался: {e}. Пробую отменить rebase.")
        subprocess.run(["git", "rebase", "--abort"], cwd=GIT_ROOT)
        return False


def git_commit_and_push(dry_run: bool = False):
    """Добавляет изменённые файлы в индекс, делает коммит и пушит с retry."""
    try:
        _run([
            "git", "add",
            os.path.relpath(GITHUBMIRROR_DIR, GIT_ROOT),
            os.path.relpath(README_PATH, GIT_ROOT),
        ])

        if not _has_staged_changes():
            log("ℹ️ Нет изменений для коммита")
            return

        _run(["git", "commit", "-m", f"🚀 Автообновление репозитория: {offset}"])
        log("✅ Коммит создан")

        if dry_run:
            log("ℹ️ Dry-run: push пропущен")
            return

        # Пробуем push. Если отклонён — pull --rebase и снова.
        for attempt in range(1, MAX_PUSH_ATTEMPTS + 1):
            result = subprocess.run(
                ["git", "push"],
                cwd=GIT_ROOT,
            )
            if result.returncode == 0:
                log("✅ Изменения запушены в репозиторий")
                return

            log(
                f"⚠️ push не удался (попытка {attempt}/{MAX_PUSH_ATTEMPTS}). "
                f"Синхронизируюсь с origin/main и повторяю."
            )
            if not _pull_rebase():
                log("❌ Не удалось синхронизироваться с origin/main. Прекращаю.")
                return

            if attempt < MAX_PUSH_ATTEMPTS:
                time.sleep(RETRY_DELAY_SEC)

        log(f"❌ push не удался после {MAX_PUSH_ATTEMPTS} попыток")

    except subprocess.CalledProcessError as e:
        log(f"❌ Ошибка git: {e}")