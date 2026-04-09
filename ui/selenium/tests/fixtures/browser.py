import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from ui.selenium.tests.utils.chrome import build_chrome_options


@pytest.fixture
def driver(request):
    headed = request.config.getoption("--ui-headed")
    options = build_chrome_options(headed=headed)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)

    if headed:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def wait(driver, wait_timeout) -> WebDriverWait:
    return WebDriverWait(driver, wait_timeout)
