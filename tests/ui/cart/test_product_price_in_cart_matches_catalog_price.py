import pytest

from ui.pages.cart_page import CartPage


class TestProductPriceInCartMatchesCatalogPrice:

    @pytest.mark.ui
    @pytest.mark.cart
    def test_product_price_in_cart_matches_catalog_price(self, driver, logged_user):
        inventory = logged_user()
        cart = CartPage(inventory.driver)
        product_id = 'sauce-labs-fleece-jacket'

        catalog_price = inventory.get_product_price(product_id)

        inventory.add_to_cart(product_id)
        inventory.open_cart()

        assert cart.is_opened(), 'Корзина не открылась'

        cart_price = cart.get_product_price(product_id)

        assert cart_price == catalog_price, (
            f'Цена в корзине {cart_price} не совпадает с ценой в каталоге {catalog_price}'
        )