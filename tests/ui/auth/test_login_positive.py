from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestLoginPage:
    def test_login_positive(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login_as('standard_user', 'secret_sauce')

        assert inventory_page.is_opened()
        assert inventory_page.items_count() == 6
