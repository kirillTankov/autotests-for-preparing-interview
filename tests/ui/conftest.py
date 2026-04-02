from datetime import datetime
from pathlib import Path
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from ui.pages.inventory_page import InventoryPage
from ui.pages.login_page import LoginPage

ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
PAGE_SOURCE_DIR = ARTIFACTS_DIR / "page_source"


def get_chrome_options(headed: bool = False) -> Options:
    options = Options()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=PasswordManagerEnabled,PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")

    if headed:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    return options


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://www.saucedemo.com/"),
        help="Базовый URL приложения",
    )
    parser.addoption(
        "--wait",
        action="store",
        default=os.getenv("WAIT_TIMEOUT", "10"),
        help="Таймаут ожидания в секундах",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=os.getenv("HEADED", "false").lower() == "true",
        help="Запускать браузер с UI",
    )


@pytest.fixture(scope="session")
def base_url(request) -> str:
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def wait_timeout(request) -> int:
    return int(request.config.getoption("--wait"))


@pytest.fixture
def driver(request):
    headed = request.config.getoption("--headed")
    options = get_chrome_options(headed=headed)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)

    if headed:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def wait(driver, wait_timeout) -> WebDriverWait:
    return WebDriverWait(driver, wait_timeout)


@pytest.fixture
def logged_user(driver, base_url):
    def _login(username="standard_user", password="secret_sauce"):
        login_page = LoginPage(driver, base_url)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login_as(username, password)

        assert inventory_page.is_opened(), "Страница Products не открылась после логина"
        return inventory_page

    return _login


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if not driver:
        return

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = item.name.replace("/", "_").replace("\\", "_").replace(":", "_")

    screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"
    page_source_path = PAGE_SOURCE_DIR / f"{test_name}_{timestamp}.html"

    try:
        driver.save_screenshot(str(screenshot_path))
        allure.attach.file(
            str(screenshot_path),
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass

    try:
        page_source_path.write_text(driver.page_source, encoding="utf-8")
        allure.attach(
            driver.page_source,
            name=f"{test_name}_page_source",
            attachment_type=allure.attachment_type.HTML,
        )
    except Exception:
        pass