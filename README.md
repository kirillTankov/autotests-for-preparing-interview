# Python AQA Pet Project

Pet project для практики и систематизации навыков Python AQA: UI и API тестирование, построение тестового фреймворка, работа с pytest, Selenium, Page Object, API Client Wrapper, конфигурацией, отчетностью и CI.

## Цели проекта

Проект создан как тренировочный automation framework, чтобы:
- повторить основные инструменты Python AQA;
- собрать понятную и расширяемую структуру тестового проекта;
- реализовать основные паттерны тестовой автоматизации;
- подготовить базу для дальнейшего добавления Allure, Playwright, CI/CD и других production-like практик.

---

## Технологии и инструменты

- Python
- Pytest
- Selenium WebDriver
- Requests
- Page Object Model
- API Client Wrapper
- Parametrization / markers / fixtures
- Скриншоты и HTML page source при падении UI тестов
- Allure Report
- Parallel execution (`pytest-xdist`)
- Retry mechanism
- GitHub Actions / Jenkins
- Playwright
- Linters / formatters / pre-commit

---

## Покрытие

### UI
UI тесты реализованы с использованием:
- Selenium WebDriver
- Page Object Model
- pytest fixtures
- автоматического сохранения артефактов при падении:
  - screenshot
  - page HTML

### API
API тесты покрывают два сервиса:
- `dummyjson` — API-заглушка для практики базовых API сценариев
- `restful-booker` — API, немного ближе к реальным кейсам

Для API реализованы:
- client wrapper
- тестовые данные
- параметризация
- проверки status code / response body / бизнес-логики ответа

---

## Архитектура проекта

```text
ui-tests/
├── api/
│   ├── clients/
│   │   ├── dummyjson/
│   │   └── restful_booker/
│   │       ├── clients/
│   │       └── test_data/
│   │           ├── auth_data.py
│   │           ├── booking_data.py
│   │           └── endpoints.py
│   └── artifacts/
│
├── config/
│
├── playwright/
│   ├── tests/
│   ├── pages/
│   ├── fixtures/
│   └── helpers/
│
├── tests/
│   ├── api/
│   │   ├── dummyjson/
│   │   └── restful_booker/
│   │       ├── conftest.py
│   │       ├── test_auth.py
│   │       └── test_booking.py
│   │
│   └── ui/
│       ├── auth/
│       ├── cart/
│       ├── catalog/
│       ├── conftest.py
│       └── test_open_page.py
│
├── ui/
│   └── pages/
│       ├── base_page.py
│       ├── cart_page.py
│       ├── checkout_step_one_page.py
│       ├── example_page.py
│       ├── inventory_page.py
│       └── login_page.py
│
├── .gitignore
└── pytest.ini
```

## Архитектурные решения

### Разделение UI и API
UI- и API-тесты разделены по директориям, чтобы:
- не смешивать разные уровни тестирования;
- упростить поддержку проекта;
- удобно запускать отдельные наборы тестов;
- проще масштабировать фреймворк.

### Отдельный модуль Playwright
Для изучения и дальнейшего внедрения Playwright в проект выделена отдельная директория `playwright/`.

Это решение позволяет:
- не смешивать Selenium- и Playwright-реализации в одной папке;
- развивать новый UI-стек независимо от текущих `pytest` UI-тестов;
- сохранить понятную структуру проекта, где существующий Python-стек не ломается;
- постепенно переносить или дублировать UI-сценарии в Playwright без хаоса в фикстурах и page objects.

На текущем этапе в `playwright/` создан только каркас директорий:
- `tests/` — будущие Playwright-тесты на Python;
- `pages/` — будущие page objects или UI-абстракции;
- `fixtures/` — будущие фикстуры;
- `helpers/` — будущие вспомогательные утилиты.

### Page Object Model
Для UI-слоя используется паттерн `Page Object`, который позволяет:
- вынести работу с элементами и действия со страницами из тестов;
- уменьшить дублирование кода;
- сделать тесты более читаемыми;
- централизованно изменять логику работы со страницами.

### API Client Wrapper
Для API-тестов используется `Client Wrapper`, который позволяет:
- инкапсулировать HTTP-запросы в отдельных клиентах;
- переиспользовать общую логику работы с API;
- сделать тесты компактнее и понятнее;
- упростить поддержку API-слоя.

### Артефакты при падении UI-тестов
При падении UI-тестов сохраняются:
- screenshot;
- HTML source страницы.

Это помогает быстрее анализировать причины падений и упрощает разбор ошибок.

## Установка

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd ui-tests
```

### 2. Создать и активировать виртуальное окружение

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Устанока зависимостей

```bash
pip install -r requirements.txt
```

### 4. Установка Playwright для Python

Когда начнется реализация Playwright-тестов, установка будет выглядеть так:

```bash
pip install playwright pytest-playwright
playwright install
```

## Запуск тестов

### Все тесты
```bash
pytest
```

### Только UI
```bash
pytest -m ui
```

### Только API
```bash
pytest -m api
```

### Подробный вывод
```bash
pytest -v
```

### Остановиться после первого падения
```bash
pytest -x
```

## Allure report

### Генерация результатов
```bash
pytest -v --alluredir=allure-results
```

### Открыть allure отчёт
```bash
allure serve allure-results
```

## Маркеры
Примеры используемых маркеров:
- smoke
- regression
- ui
- api

Если маркеры зарегистрированы в pytest.ini, это позволяет:
- удобно собирать test suites;
- запускать нужные группы тестов;
- разделять быстрые и полные прогоны.
