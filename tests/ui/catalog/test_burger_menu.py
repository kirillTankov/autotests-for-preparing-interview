import pytest


class TestBurgerMenu:

    @pytest.mark.catalog
    def test_burger_menu(self, driver, logged_user):
        inventory = logged_user()

        inventory.open_menu()
        assert inventory.is_burger_menu_open()

        inventory.close_menu()
        assert not inventory.is_burger_menu_open()


