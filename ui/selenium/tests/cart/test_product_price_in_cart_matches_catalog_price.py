import allure
import pytest

from ui.selenium.pages.cart_page import CartPage


class TestProductPriceInCartMatchesCatalogPrice:

    @allure.epic("UI")
    @allure.feature("Cart")
    @allure.story("Синхронизация цен")
    @allure.title("Цена товара в корзине совпадает с ценой в каталоге")
    @pytest.mark.ui
    @pytest.mark.cart
    def test_product_price_in_cart_matches_catalog_price(self, driver, logged_user):
        product_id = 'sauce-labs-fleece-jacket'

        with allure.step("Авторизация"):
            inventory = logged_user()

        cart = CartPage(inventory.driver)

        with allure.step(f"Получить цену товара '{product_id}' в каталоге"):
            catalog_price = inventory.get_product_price(product_id)

        with allure.step(f"Добавить товар '{product_id}' в корзину"):
            inventory.add_to_cart(product_id)

        with allure.step("Открыть корзину"):
            inventory.open_cart()

        with allure.step("Проверить, что страница коризны открыта"):
            assert cart.is_opened(), 'Корзина не открылась'

        with allure.step(f"Получить цену товара '{product_id}' в корзине"):
            cart_price = cart.get_product_price(product_id)

        with allure.step("Проверить совпадение цены в каталоге и корзине"):
            assert cart_price == catalog_price, (
                f'Цена в корзине {cart_price} не совпадает с ценой в каталоге {catalog_price}'
            )
