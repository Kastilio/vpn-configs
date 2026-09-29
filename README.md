# 📖 Описание проекта

<p align="center">
  <a href="https://github.com/Kastilio/vpn-configs"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <a href="https://github.com/Kastilio/vpn-configs/stargazers"><img src="https://img.shields.io/github/stars/Kastilio/vpn-configs?style=for-the-badge" alt="GitHub stars"></a>
  <img src="https://img.shields.io/github/forks/Kastilio/vpn-configs?style=for-the-badge" alt="GitHub forks">
  <a href="https://github.com/Kastilio/vpn-configs/watchers">
  <img src="https://img.shields.io/github/watchers/Kastilio/vpn-configs?style=for-the-badge" alt="GitHub Watchers"></a>
  <a href="https://github.com/Kastilio/vpn-configs/pulls"><img src="https://img.shields.io/github/issues-pr/Kastilio/vpn-configs?style=for-the-badge" alt="GitHub pull requests"></a>
  <a href="https://github.com/Kastilio/vpn-configs/issues"><img src="https://img.shields.io/github/issues/Kastilio/vpn-configs?style=for-the-badge" alt="GitHub issues"></a>
</p>

> **Дисклеймер.** Репозиторий содержит публично доступные конфигурации, собранные из открытых источников. Материалы предоставлены исключительно в ознакомительных и образовательных целях, для тестирования совместимости VPN-клиентов. Автор не призывает к нарушению законодательства и не несёт ответственности за использование материалов третьими лицами. Пользователь самостоятельно несёт ответственность за соблюдение законов своей юрисдикции.

Автоматически обновляемая коллекция публичных конфигураций для VPN-клиентов (`V2Ray` / `VLESS` / `Hysteria` / `Trojan` / `VMess` / `Reality` / `Shadowsocks`).

Каждый конфиг — это TXT-подписка, которую можно импортировать практически в любой современный клиент (`v2rayNG`, `NekoRay`, `Throne`, `v2rayN`, `V2Box`, `v2RayTun`, `Hiddify` и др.).

Конфиги обновляются каждые **9 минут** с помощью GitHub Actions, поэтому ссылки из раздела **«📋 Общий список актуальных конфигов»** всегда актуальны.

## 📑 Содержание
- [📖 Описание проекта](#-описание-проекта)
  - [📑 Содержание](#-содержание)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [📊 Статус конфигов](#-статус-конфигов)
  - [📊 Статистика репозитория](#-статистика-репозитория)
  - [⚙️ Как это работает](#️-как-это-работает)
  - [🗂 Структура репозитория](#-структура-репозитория)
  - [🔧 Локальный запуск генератора](#-локальный-запуск-генератора)
- [🗂️ Общее меню гайдов репозитория](#️-общее-меню-гайдов-репозитория)
- [📜 Лицензия](#-лицензия)

---

## 🚀 Быстрый старт
1. Скопируйте нужную ссылку из раздела **«📋 Общий список актуальных конфигов»**.
2. Импортируйте её в ваш **VPN-клиент** (см. инструкции ниже).
3. Выберите сервер с минимальным пингом и подключайтесь.

---

## 📊 Статус конфигов

> **⚠️ Внимание!** Эта таблица показывает только **источники** и статус обновления конфигов. **Не копируйте ссылки отсюда!**
> Для использования копируйте ссылки из раздела **«📋 Общий список актуальных конфигов»** ниже.

| № | Файл | Источник | Время | Дата |
|--|--|--|--|--|
| 1 | [`1.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/1.txt) | [sakha1370/OpenRay](https://github.com/sakha1370/OpenRay/raw/refs/heads/main/output/all_valid_proxies.txt) | 21:43 (МСК) | 29.09.2026 |
| 2 | [`2.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/2.txt) | [sevcator/5ubscrpt10n](https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt) | 03:10 (МСК) | 30.07.2026 |
| 3 | [`3.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/3.txt) | [yitong2333/proxy-minging](https://raw.githubusercontent.com/yitong2333/proxy-minging/refs/heads/main/v2ray.txt) | 21:43 (МСК) | 29.09.2026 |
| 4 | [`4.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/4.txt) | [acymz/AutoVPN](https://raw.githubusercontent.com/acymz/AutoVPN/refs/heads/main/data/V2.txt) | 21:43 (МСК) | 29.09.2026 |
| 5 | [`5.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/5.txt) | [miladtahanian/V2RayCFGDumper](https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/refs/heads/main/sub.txt) | 21:43 (МСК) | 29.09.2026 |
| 6 | [`6.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/6.txt) | [roosterkid/openproxylist](https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt) | 21:43 (МСК) | 29.09.2026 |
| 7 | [`7.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/7.txt) | [Epodonios/v2ray-configs](https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt) | 21:43 (МСК) | 29.09.2026 |
| 8 | [`8.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/8.txt) | [ShatakVPN/ConfigForge-V2Ray](https://github.com/ShatakVPN/ConfigForge-V2Ray/raw/refs/heads/main/configs/vless.txt) | 21:43 (МСК) | 29.09.2026 |
| 9 | [`9.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/9.txt) | [mohamadfg-dev/telegram-v2ray-configs-collector](https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/refs/heads/main/category/vless.txt) | 21:43 (МСК) | 29.09.2026 |
| 10 | [`10.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/10.txt) | [mheidari98/.proxy](https://raw.githubusercontent.com/mheidari98/.proxy/refs/heads/main/vless) | 21:43 (МСК) | 29.09.2026 |
| 11 | [`11.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/11.txt) | [youfoundamin/V2rayCollector](https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt) | 16:20 (МСК) | 29.09.2026 |
| 12 | [`12.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/12.txt) | [VOID-Anonymity/V.O.I.D-VPN_Bypass](https://github.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/raw/refs/heads/main/url_work.txt) | 21:43 (МСК) | 29.09.2026 |
| 13 | [`13.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/13.txt) | [cbusifabcap/daily_free_vpn](https://github.com/cbusifabcap/daily_free_vpn/raw/refs/heads/main/Z.txt) | 21:43 (МСК) | 29.09.2026 |
| 14 | [`14.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/14.txt) | [LalatinaHub/Mineral](https://github.com/LalatinaHub/Mineral/raw/refs/heads/master/result/nodes) | 02:38 (МСК) | 10.08.2026 |
| 15 | [`15.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/15.txt) | [miladtahanian/Config-Collector](https://raw.githubusercontent.com/miladtahanian/Config-Collector/refs/heads/main/mixed_iran.txt) | 21:43 (МСК) | 29.09.2026 |
| 16 | [`16.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/16.txt) | [Pawdroid/Free-servers](https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub) | 21:43 (МСК) | 29.09.2026 |
| 17 | [`17.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/17.txt) | [MhdiTaheri/V2rayCollector_Py](https://github.com/MhdiTaheri/V2rayCollector_Py/raw/refs/heads/main/sub/Mix/mix.txt) | 21:43 (МСК) | 29.09.2026 |
| 18 | [`18.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/18.txt) | [free18/v2ray](https://raw.githubusercontent.com/free18/v2ray/refs/heads/main/v.txt) | 09:43 (МСК) | 29.09.2026 |
| 19 | [`19.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/19.txt) | [MhdiTaheri/V2rayCollector](https://github.com/MhdiTaheri/V2rayCollector/raw/refs/heads/main/sub/mix) | 21:43 (МСК) | 29.09.2026 |
| 20 | [`20.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/20.txt) | [Argh94/Proxy-List](https://github.com/Argh94/Proxy-List/raw/refs/heads/main/All_Config.txt) | 21:43 (МСК) | 29.09.2026 |
| 21 | [`21.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/21.txt) | [shabane/kamaji](https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt) | 03:32 (МСК) | 10.08.2026 |
| 22 | [`22.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/22.txt) | [wuqb2i4f/xray-config-toolkit](https://raw.githubusercontent.com/wuqb2i4f/xray-config-toolkit/main/output/base64/mix-uri) | 16:20 (МСК) | 29.09.2026 |
| 23 | [`23.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/23.txt) | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia/raw/refs/heads/main/BLACK_VLESS_RUS.txt) | 21:43 (МСК) | 29.09.2026 |
| 24 | [`24.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/24.txt) | [Mr-Meshky/vify](https://github.com/Mr-Meshky/vify/raw/refs/heads/main/configs/vless.txt) | 21:43 (МСК) | 29.09.2026 |
| 25 | [`25.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/25.txt) | [V2RayRoot/V2RayConfig](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt) | 12:55 (МСК) | 07.07.2026 |
| 26 | [`26.txt`](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt) | [Настройка SNI/CIDR](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt) | 21:43 (МСК) | 29.09.2026 |

## 📊 Статистика репозитория
| Показатель | Значение |
|--|--|
| Просмотры (14Д) | 82 |
| Клоны (14Д) | 500 |
| Уникальные клоны (14Д) | 238 |
| Уникальные посетители (14Д) | 30 |

## ⚙️ Как это работает
1. **GitHub Actions** запускает скрипт каждые **9 минут** (автоматически) или вручную.
2. Скрипт скачивает конфиги из **25 публичных источников** параллельно.
3. Каждый конфиг фильтруется: декодируется Base64, проверяется на наличие протоколов (`vmess://`, `vless://`, `trojan://`, `ss://`, `hysteria://` и др.), удаляются конфиги с `allowinsecure=1`.
4. **26-й файл** формируется отдельно: из файлов 1–25 отбираются только конфиги, соответствующие заданным SNI/CIDR-правилам, и объединяются с дополнительными источниками.
5. Ссылки на скачивание **v2rayNG**, **Throne** и **Visual C++ Runtimes** автоматически обновляются с GitHub API.
6. Статистика репозитория (просмотры, клоны) обновляется в README.md.
7. Все изменения коммитятся и пушатся в репозиторий.

## 🗂 Структура репозитория
```text
.github/workflows/   — CI/CD (авто-обновление каждые 9 мин)
githubmirror/        — сгенерированные .txt конфиги (26 файлов)
qr-codes/            — PNG-версии конфигов для импорта по QR (26 файлов)
source/              — исходный код и конфигурации генератора
 ├─ main.py          — основной скрипт генерации
 ├─ requirements.txt — зависимости Python
 ├─ config/          — конфигурации
 │   ├─ urls.json        — список источников для конфигов 1-25
 │   ├─ 26_urls.json     — источники для конфига №26
 │   └─ sni_domains.json — список доменов для SNI (~985 доменов)
 └─ src/             — модули генератора
     ├─ __init__.py        — инициализация пакета
     ├─ config.py          — пути и загрузка конфигурации
     ├─ file_manager.py    — скачивание, фильтрация и сохранение файлов
     ├─ git_ops.py         — коммит и push изменений
     ├─ github_api.py      — статистика репозитория через GitHub API
     ├─ logger.py          — логирование и таймстемпы
     ├─ network.py         — HTTP-сессия с retry и fallback
     ├─ parser.py          — фильтрация небезопасных конфигов
     ├─ readme_updater.py  — автообновление README.md
     └─ release_fetcher.py — получение актуальных ссылок на скачивание
LICENSE              — лицензия GPL-3.0
README.md            — этот файл
```

---

## 🔧 Локальный запуск генератора
```bash
git clone https://github.com/Kastilio/vpn-configs
cd vpn-configs/source
python -m pip install -r requirements.txt
export MY_TOKEN=<GITHUB_TOKEN>   # токен с правом repo, чтобы пушить изменения
python main.py                  # конфиги появятся в ../githubmirror
```

> **Важно!** В файле `source/src/config.py` задайте `REPO_NAME = "Kastilio/vpn-configs"`.

---

# 🗂️ Общее меню гайдов репозитория

<details>

<summary>👩‍💻 Исходный код для генерации актуальных конфигов</summary>

Ссылка на исходный код — [Ссылка](https://github.com/Kastilio/vpn-configs/tree/main/source)

</details>


---
<details>

<summary>📋 Общий список актуальных конфигов</summary>

> Рекомендованные списки: **[1](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/1.txt)**, **[6](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/6.txt)**, **[22](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/22.txt)**, **[23](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/23.txt)**, **[24](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/24.txt)** и **[25](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/25.txt)**.

> SNI/CIDR: **[26](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt)**.

 - [ ] **Актуальные**

1) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/1.txt`
2) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/2.txt`
3) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/3.txt`
4) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/4.txt`
5) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/5.txt`
6) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/6.txt`
7) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/7.txt`
8) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/8.txt`
9) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/9.txt`
10) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/10.txt`
11) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/11.txt`
12) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/12.txt`
13) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/13.txt`
14) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/14.txt`
15) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/15.txt`
16) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/16.txt`
17) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/17.txt`
18) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/18.txt`
19) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/19.txt`
20) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/20.txt`
21) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/21.txt`
22) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/22.txt`
23) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/23.txt`
24) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/24.txt`
25) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/25.txt`
26) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt`

🔗 [Ссылка на QR-коды актуальных конфигов](https://github.com/Kastilio/vpn-configs/tree/main/qr-codes)
</details>


---
<details>

<summary>📱 Гайд для Android</summary>

**1.** Скачиваем **«v2rayNG»** — [Ссылка](https://github.com/2dust/v2rayNG/releases/download/2.2.6/v2rayNG_2.2.6_arm64-v8a.apk)

**2.** Копируем в буфер обмена:

> Рекомендованные списки: **[1](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/1.txt)**, **[6](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/6.txt)**, **[22](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/22.txt)**, **[23](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/23.txt)**, **[24](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/24.txt)** и **[25](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/25.txt)**.

> SNI/CIDR: **[26](https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt)**.

 - [ ] **Актуальные**

1) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/1.txt`
2) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/2.txt`
3) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/3.txt`
4) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/4.txt`
5) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/5.txt`
6) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/6.txt`
7) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/7.txt`
8) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/8.txt`
9) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/9.txt`
10) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/10.txt`
11) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/11.txt`
12) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/12.txt`
13) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/13.txt`
14) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/14.txt`
15) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/15.txt`
16) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/16.txt`
17) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/17.txt`
18) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/18.txt`
19) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/19.txt`
20) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/20.txt`
21) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/21.txt`
22) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/22.txt`
23) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/23.txt`
24) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/24.txt`
25) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/25.txt`
26) `https://github.com/Kastilio/vpn-configs/raw/refs/heads/main/githubmirror/26.txt`

**3.** Заходим в приложение **«v2rayNG»** и в правом верхнем углу нажимаем на ➕, а затем выбираем **«Импорт из буфера обмена»**.

**4.** Нажимаем **«справа сверху на три точки»**, а затем **«Проверить задержку профилей»**, после окончания проверки в этом же меню нажмите на **«Сортировать по результатам теста»**.

**5.** Выбираем нужный вам сервер и затем нажимаем на кнопку ▶️ в правом нижнем углу.

</details>

<details>

<summary>📺 Гайд для Android TV</summary>

**1.** Скачиваем **«v2rayNG»** — [Ссылка](https://github.com/2dust/v2rayNG/releases/download/2.2.6/v2rayNG_2.2.6_armeabi-v7a.apk)

> Рекомендованные **«QR-коды»**: **[1](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/1.png)**, **[6](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/6.png)**, **[22](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/22.png)**, **[23](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/23.png)**, **[24](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/24.png)** и **[25](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/25.png)**.

> SNI/CIDR: **[26](https://github.com/Kastilio/vpn-configs/blob/main/qr-codes/26.png)**.

**2.** Скачиваем **«QR-коды»** актуальных конфигов — [Ссылка](https://github.com/Kastilio/vpn-configs/tree/main/qr-codes)

**3**. Заходим в приложение **«v2rayNG»** и в правом верхнем углу нажимаем на ➕, а затем выбираем **«Импорт из QR-кода»**, выбираем картинку нажав на иконку фото в правом верхнем углу.

**4.** Нажимаем **«справа сверху на три точки»**, а затем **«Проверить задержку профилей»**, после окончания проверки в этом же меню нажмите на **«Сортировать по результатам теста»**.

**5.** Выбираем нужный вам сервер и затем нажимаем на кнопку ▶️ в правом нижнем углу.

</details>

<details>

<summary>⚠ Если нет интернета при подключении к VPN в v2rayNG</summary>

**1.** На рабочем столе зажимаем на иконке **«v2rayNG»** и нажимаем на пункт **«О приложении»**.

**2.** Нажимаем на кнопку **«Остановить»** и заново запускаем **«v2rayNG»**.

</details>

<details>

<summary>⚠ Если не появились конфиги при добавлении VPN в v2rayNG</summary>

**1.** Нажмите на **«три полоски»** в **«левом верхнем углу»**.

**2.** Нажимаем на кнопку **«Группы»**.

**3.** Нажимаем на **«иконку кружка со стрелкой»** в **«верхнем правом углу»** и дожидаемся окончания обновления.

</details>

<details>

<summary>⚠ Фикс ошибки "Cбой проверки интернет-соединения: net/http: 12X handshake timeout"</summary>

**1.** На рабочем столе зажимаем на иконке **«v2rayNG»** и нажимаем на пункт **«О приложении»**.

**2.** Нажимаем на кнопку **«Остановить»** и заново запускаем **«v2rayNG»**.

</details>

<details>

<summary>⚠ Фикс ошибки "Fail to detect internet connection: io: read/write closed pipe"</summary>

**1.** На рабочем столе зажимаем на иконке **«v2rayNG»** и нажимаем на пункт **«О приложении»**.

**2.** Нажимаем на кнопку **«Остановить»** и заново запускаем **«v2rayNG»**.

**3.** Нажимаем **«справа сверху на три точки»**, а затем **«Проверить задержку профилей»**, после окончания проверки в этом же меню нажмите на **«Сортировать по результатам теста»**.

**4.** Выбираем нужный вам сервер и затем нажимаем на кнопку ▶️ в правом нижнем углу.

</details>

<details>

<summary>🔄 Обновление конфигов в v2rayNG</summary>

**1.** Нажимаем на **«иконку трех полосок»** в **«левом верхнем углу»**.

**2.** Выбираем вкладку **«Группы»**.

**3.** Нажимаем на **«иконку кружка со стрелкой»** в **«правом верхнем углу»**.

</details>


---
<details>

<summary>🖥 Гайд для Windows, Linux</summary>

**1.** Скачиваем **«Throne»** — [Windows 10/11](https://github.com/throneproj/Throne/releases/download/1.3.1/Throne-1.3.1-windows64.zip) / [Windows 7/8/8.1](https://github.com/throneproj/Throne/releases/download/1.3.1/Throne-1.3.1-windowslegacy64.zip) / [Linux](https://github.com/throneproj/Throne/releases/download/1.3.1/Throne-1.3.1-linux-amd64.zip)

**2.** Копируем в буфер обмена:

> Рекомендованные списки: **[1](https://github.com/Kastilio/vpn-configs/raw/ref