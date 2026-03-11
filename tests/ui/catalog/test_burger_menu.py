import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestBurgerMenu:

    @pytest.mark.catalog
    def test_burger_menu(self, driver, logged_user):

        inventory = logged_user()
        assert inventory.is_opened(), 'Страница Products не открылась'

        inventory.open_menu()
        assert inventory.is_burger_menu_open()

        inventory.close_menu()
        assert not inventory.is_burger_menu_open()


