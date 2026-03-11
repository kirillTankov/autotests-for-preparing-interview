import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestAddToCart:

    @pytest.mark.cart
    def test_add_to_cart(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        product_id = 'sauce-labs-fleece-jacket'

        login.open()
        login.login_as("standard_user", "secret_sauce")

        assert inventory.is_opened(), 'Страница Products не открылась'

        inventory.add_to_cart(product_id)
        assert inventory.is_product_added(product_id), 'Товар не был добавлен в корзину'
        assert inventory.get_cart_badge_text() == '1', 'Счетчик корзины должен быть равен 1'

    @pytest.mark.cart
    def test_add_multiple_products_to_cart(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        products = [
            "sauce-labs-backpack",
            "sauce-labs-bike-light",
            "sauce-labs-fleece-jacket",
        ]

        login.open()
        login.login_as("standard_user", "secret_sauce")

        assert inventory.is_opened(), 'Страница Products не открылась'

        for product_id in products:
            inventory.add_to_cart(product_id)

        for product_id in products:
            assert inventory.is_product_added(product_id), f"Товар {product_id} не был добавлен в корзину"

        assert inventory.get_cart_badge_text() == str(len(products)), \
            f"Счетчик корзины должен быть {len(products)}"
