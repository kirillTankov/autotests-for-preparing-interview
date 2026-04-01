import allure
import pytest


class TestAddToCart:

    @allure.epic("UI")
    @allure.feature("Cart")
    @allure.story("Добавление товара")
    @allure.title("Товар добавляется в корзину")
    @pytest.mark.cart
    def test_add_to_cart(self, driver, logged_user):
        product_id = 'sauce-labs-fleece-jacket'

        with allure.step("Авторизоваться в системе"):
            inventory = logged_user()

        with allure.step(f"Добавить товар '{product_id}' в корзину"):
            inventory.add_to_cart(product_id)

        with allure.step("Проверка, что товар добавлен в коризну"):
            assert inventory.is_product_added(product_id), 'Товар не был добавлен в корзину'

        with allure.step("Проверить, что счетчик корзины равен 1"):
            assert inventory.get_cart_badge_text() == '1', 'Счетчик корзины должен быть равен 1'

    @allure.epic("UI")
    @allure.feature("Cart")
    @allure.story("Добавление нескольких товаров")
    @allure.title("Несколько товаров добавляются в корзину")
    @pytest.mark.cart
    def test_add_multiple_products_to_cart(self, driver, logged_user):
        products = [
            "sauce-labs-backpack",
            "sauce-labs-bike-light",
            "sauce-labs-fleece-jacket",
        ]

        with allure.step("Авторизоваться в системе"):
            inventory = logged_user()

        with allure.step("Добавить товары в корзину"):
            for product_id in products:
                inventory.add_to_cart(product_id)

        with allure.step("Проверить, что все товары добавлены в корзину"):
            for product_id in products:
                assert inventory.is_product_added(product_id), (
                    f"Товар {product_id} не был добавлен в корзину"
                )

        with allure.step(f"Проверить, что счетчик корзины равен {len(products)}"):
            assert inventory.get_cart_badge_text() == str(len(products)), (
                f"Счетчик корзины должен быть {len(products)}"
            )