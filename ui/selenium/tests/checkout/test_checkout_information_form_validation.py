import allure
import pytest

from ui.selenium.pages.cart_page import CartPage
from ui.selenium.pages.checkout_step_one_page import CheckoutStepOne


class TestCheckoutInformationFormValidation:
    @allure.epic("UI")
    @allure.feature("Checkout")
    @allure.story("Валидация формы Your Information")
    @allure.title("Проверка валидации полей \"Checkout: Your Information\" формы")
    @pytest.mark.ui
    @pytest.mark.parametrize(
        'first_name, last_name, postal_code, expected_error',
        [
            ("", "Ivanov", "12345", "Error: First Name is required"),
            ("Ivan", "", "12345", "Error: Last Name is required"),
            ("Ivan", "Ivanov", "", "Error: Postal Code is required"),
        ],
        ids=[
            "empty_first_name",
            "empty_last_name",
            "empty_postal_code",
        ]
    )
    def test_checkout_information_form_validation(
            self,
            driver,
            logged_user,
            first_name,
            last_name,
            postal_code,
            expected_error
    ):
        cart = CartPage(driver)
        checkout_step_one = CheckoutStepOne(driver)

        product_id = 'sauce-labs-bolt-t-shirt'

        with allure.step("Авторизация"):
            inventory = logged_user("standard_user", "secret_sauce")

        with allure.step(f"Добавить товар {product_id} в корзину"):
            inventory.add_to_cart(product_id)

        with allure.step("Открыть корзину"):
            inventory.open_cart()

        with allure.step("Проверить открытие страницы корзины"):
            assert cart.is_opened(), 'Страница Your Cart не открылась'

        with allure.step("Перейти к оформлению заказа"):
            cart.click_checkout()

        with allure.step("Проверить открытие формы Checkout: Your Information"):
            assert checkout_step_one.is_opened(), 'Страница Checkout: Your Information не открылась'

        with allure.step("Заполнить форму"):
            with allure.step(f"Заполнить поле First Name значением: {first_name}"):
                checkout_step_one.fill_first_name(first_name)
            with allure.step(f"Заполнить поле Last Name значением: {last_name}"):
                checkout_step_one.fill_last_name(last_name)
            with allure.step(f"Заполнить поле Postal Code значением: {postal_code}"):
                checkout_step_one.fill_postal_code(postal_code)

        with allure.step("Нажать кнопку Continue"):
            checkout_step_one.click_continue()

        with allure.step("Проверить сообщение об ошибки"):
            actual_error = checkout_step_one.get_error_message()
            assert expected_error in actual_error, f"Ожидал ошибку: {expected_error}, получил: {actual_error}"

