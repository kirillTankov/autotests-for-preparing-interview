import pytest

from ui.selenium.pages.inventory_page import InventoryPage
from ui.selenium.pages.login_page import LoginPage


@pytest.fixture
def logged_user(driver, base_url):
    def _login(username="standard_user", password="secret_sauce"):
        login_page = LoginPage(driver, base_url)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login_as(username, password)

        assert inventory_page.is_opened(), "Page Products was not opened after login"
        return inventory_page

    return _login
