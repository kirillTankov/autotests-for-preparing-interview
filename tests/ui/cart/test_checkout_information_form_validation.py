import pytest

from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOne


class TestCheckoutInformationFormValidation:
    @pytest.mark.ui
    @pytest.mark.parametrize(
        'first_name, last_name, postal_code, error',
        [
            ("", "Ivanov", "12345", "Error: First Name is required"),
            ("Ivan", "", "12345", "Error: Last Name is required"),
            ("Ivan", "Ivanov", "", "Error: Postal Code is required"),
        ],
    )
    def test_checkout_information_form_validation(
            self,
            driver,
            logged_user,
            first_name,
            last_name,
            postal_code,
            error
    ):
        inventory = logged_user("standard_user", "secret_sauce")
        cart = CartPage(driver)
        checkout_step_one = CheckoutStepOne(driver)
        product_id = 'sauce-labs-bolt-t-shirt'

        assert inventory.is_opened(), 'Страница Products не открылась'

        inventory.add_to_cart(product_id)
        inventory.open_cart()
        assert cart.is_opened(), 'Страница Your Cart не открылась'

        cart.click_checkout()
        assert checkout_step_one.is_opened(), 'Страница Checkout: Your Information не открылась'

        checkout_step_one.fill_first_name(first_name)
        checkout_step_one.fill_last_name(last_name)
        checkout_step_one.fill_postal_code(postal_code)
        checkout_step_one.click_continue()

        assert error in checkout_step_one.get_error_message()

