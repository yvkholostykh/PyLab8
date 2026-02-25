# PyLab8
PyLab8
# Взаимодействие в WWW: анализ трафика и эксплуатация XSS с помощью Scapy

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-000000?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSI+PHBhdGggZD0iTTE2IDJDMTAuNDggMiA2IDYuNDggNiAxMkM2IDE3LjUyIDEwLjQ4IDIyIDE2IDIyQzIxLjUyIDIyIDI2IDE3LjUyIDI2IDEyQzI2IDYuNDggMjEuNTIgMiAxNiAyMkMxMS40OCAyIDYgNi40OCA2IDEyTDIzIDEySDlMMTYgMnoiIGZpbGw9IiMwMDAiLz48L3N2Zz4=)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white)
![Google Gruyere](https://img.shields.io/badge/Google_Gruyere-4285F4?logo=google&logoColor=white)

## Описание проекта

Проект посвящён изучению взаимодействия с веб‑сервисами, анализу сетевого трафика и эксплуатации уязвимостей типа cross‑site scripting (XSS) на учебном сайте Google Gruyere с использованием инструмента Scapy в Python 3.

## Иконки и изображения

В репозитории присутствуют следующие изображения:
* `images/setup.png` — скриншот настройки окружения;
* `images/xss_attack.png` — демонстрация успешной XSS‑атаки;
* `images/traffic_analysis.png` — анализ перехваченного трафика в Wireshark.

![Настройка окружения](images/setup.png)
*Рисунок 1: Настройка окружения в VS Code*

![XSS‑атака](images/xss_attack.png)
*Рисунок 2: Успешная XSS‑атака в браузере*

## Цель задания

Научиться использовать инструмент Scapy для:
* анализа сетевого трафика;
* эксплуатации уязвимостей XSS на учебном сайте Google Gruyere.

## Инструменты

* **Python 3** — язык программирования.
* **Visual Studio Code** — среда разработки.
* **Scapy** — библиотека для анализа и манипуляции сетевыми пакетами.
* **Google Gruyere** — учебный веб‑сайт для изучения уязвимостей.
* **Браузерные инструменты разработчика** — для анализа веб‑страниц.
* **Wireshark** (опционально) — для визуального анализа .pcap‑файлов.

## Установка и настройка окружения

### Предварительные требования

* Установленный Python 3 (с `pip`).
* Установленный Visual Studio Code.
* Доступ в интернет.
Для расширенного анализа HTTP‑трафика установите дополнительные пакеты:
pip install requests gzip
Настройка для Linux / WSL
Для корректного перехвата трафика временно отключите отправку TCP RST‑пакетов:
sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
После завершения работы обязательно верните правило обратно:
sudo iptables -D OUTPUT -p tcp --tcp-flags RST RST -j DROP
Настройка для Windows
Рекомендуется использовать WSL (Windows Subsystem for Linux) для работы со Scapy.

Установите WSL.

Запустите дистрибутив Linux (например, Ubuntu).

Выполните установку Scapy внутри WSL:
sudo apt update
sudo apt install python3-pip
pip3 install scapy requests
Инструкция по запуску
Этап 1. Запуск Google Gruyere
Перейдите на  или запустите локальный инстанс согласно документации.

Убедитесь, что сайт доступен в браузере.

Этап 2. Перехват трафика с помощью Scapy
Откройте файл sniff_traffic.py в VS Code.

Запустите скрипт с правами суперпользователя (требуется для Scapy):
sudo python3 sniff_traffic.py
Скрипт начнёт перехват трафика и сохранит его в файл capture.pcap.
Этап 3. Взаимодействие с Google Gruyere и XSS‑атака
Открывайте страницы, отправляйте формы, вводите данные.

Найдите поля ввода (комментарии, поиск и т. д.).

Введите полезную нагрузку, например:
<script>alert('XSS')</script>
Или:
<img src="x" onerror="alert('XSS')">
Остановите перехват трафика: нажмите Ctrl + C в терминале.
Этап 4. Анализ сохранённого трафика
Запустите скрипт анализа:
python3 analyze_pcap.py capture.pcap
Скрипт выведет информацию о HTTP‑запросах и ответах, включая XSS‑полезные нагрузки.
### Установка пакетов

1. Откройте терминал в VS Code (`Ctrl + ~`).
2. Установите Scapy:
   ```bash
   pip install scapy
