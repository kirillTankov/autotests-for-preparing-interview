import os
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait

from inventory_page import InventoryPage
from login_page import LoginPage

ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
PAGE_SOURCE_DIR = ARTIFACTS_DIR / "page_source"


def build_chrome_options(headed: bool = False) -> ChromeOptions:
    options = ChromeOptions()

    # Stable defaults for UI automation
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=TranslateUI")

    # Headless by default, headed if explicitly requested
    if not headed:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    user_data_dir = os.getenv("CHROME_USER_DATA_DIR")
    if user_data_dir:
        options.add_argument(f"--user-data-dir={user_data_dir}")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.autofill_profile_enabled": False,
        "profile.autofill_credit_card_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    return options


def create_chrome_driver(headed: bool = False) -> webdriver.Chrome:
    options = build_chrome_options(headed=headed)

    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path:
        service = ChromeService(executable_path=chromedriver_path)
        return webdriver.Chrome(service=service, options=options)

    return webdriver.Chrome(options=options)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--base-url", action="store", default="https://www.saucedemo.com/", help="Base URL")
    parser.addoption("--wait", action="store", default="10", help="Default explicit wait timeout in seconds")
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode"
    )

@pytest.fixture
def logged_user(driver):
    def _login(username="standard_user", password="secret_sauce"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login_as(username, password)
        return InventoryPage(driver)
    return _login

@pytest.fixture(scope="session")
def base_url(request) -> str:
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def wait_timeout(request) -> int:
    return int(request.config.getoption("--wait"))


@pytest.fixture
def driver(request, wait_timeout):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser != "chrome":
        raise ValueError(f"Unsupported browser: {browser}")

    drv = create_chrome_driver(headed=headed)
    drv.implicitly_wait(0)

    if headed:
        drv.maximize_window()

    yield drv
    drv.quit()


@pytest.fixture
def wait(driver, wait_timeout) -> WebDriverWait:
    return WebDriverWait(driver, wait_timeout)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call" or not rep.failed:
        return

    drv = item.funcargs.get("driver")
    if not drv:
        return

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = item.name.replace("/", "_").replace("\\", "_").replace(":", "_")

    screenshot_path = SCREENSHOTS_DIR / f"{safe_test_name}_{ts}.png"
    page_source_path = PAGE_SOURCE_DIR / f"{safe_test_name}_{ts}.html"

    try:
        drv.save_screenshot(str(screenshot_path))
    except Exception:
        pass

    try:
        page_source_path.write_text(drv.page_source, encoding="utf-8")
    except Exception:
        pass