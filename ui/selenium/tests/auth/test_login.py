import allure
import pytest

from ui.selenium.pages.inventory_page import InventoryPage
from ui.selenium.pages.login_page import LoginPage


@allure.epic("UI")
@allure.feature("Login")
class TestLoginPage:

    @allure.story("Успешная авторизация")
    @allure.title("Пользователь может войти с валидными данными")
    @pytest.mark.ui
    @pytest.mark.auth
    def test_login_positive(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        inventory_page = InventoryPage(driver)

        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Авторизоваться под standard_user"):
            login_page.login_as('standard_user', 'secret_sauce')

        with allure.step("Проверить, что открылась страница каталога"):
            assert inventory_page.is_opened(), "Старница каталога не открылась"

        with allure.step("Проверить, что отображаются 6 товаров"):
            assert inventory_page.items_count() == 6, "Количество товаров не равно 6"

    @allure.story("Ошибка авторизации")
    @allure.title("Заблокированный пользователь не может войти в систему")
    @pytest.mark.ui
    @pytest.mark.auth
    def test_login_negative(self, driver, base_url):
        login_page = LoginPage(driver, base_url)

        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Ввести username 'locked_out_user'"):
            login_page.fill_field_username("locked_out_user")

        with allure.step("Ввести пароль"):
            login_page.fill_field_password("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            login_page.click_login_button()

        with allure.step("Проверить текст ошибки о заблокированном пользователе"):
            assert "locked out" in login_page.get_error_text().lower(), (
                "Сообщение об ошибке для заблокированного пользователя не отображается"
            )
