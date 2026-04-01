import allure
import pytest


class TestBurgerMenu:

    @allure.epic("UI")
    @allure.feature("Catalog")
    @allure.story("Burger menu")
    @allure.title("Меню открывается и закрывается")
    @pytest.mark.catalog
    def test_burger_menu(self, driver, logged_user):
        with allure.step("Авторизоваться в системе"):
            inventory = logged_user()

        with allure.step("Открыть меню"):
            inventory.open_menu()

        with allure.step("Проверить, что меню открыто"):
            assert inventory.is_burger_menu_open()

        with allure.step("Закрыть меню"):
            inventory.close_menu()

        with allure.step("Проверить, что меню закрыто"):
            assert not inventory.is_burger_menu_open()


