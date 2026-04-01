import allure
import pytest


@allure.epic("UI")
@allure.feature("Catalog")
class TestSortPrice:

    @allure.story("Сортировка по цене")
    @allure.title("Товары сортируются по цене: {sort_value}")
    @pytest.mark.catalog
    @pytest.mark.sorting
    @pytest.mark.parametrize(
        "sort_value, reverse",
        [
            ("lohi", False),
            ("hilo", True),
        ],
        ids=["price_low_to_high", "price_high_to_low"]
    )
    def test_sort_price(self, driver, logged_user, sort_value, reverse):
        with allure.step("Авторизоваться в системе"):
            inventory = logged_user()

        with allure.step(f"Выбрать сортировку '{sort_value}'"):
            inventory.sort_by(sort_value)

        with allure.step("Получить список цен товаров"):
            prices = inventory.get_prices()

        with allure.step("Проверить корректность сортировки цен"):
            assert prices == sorted(prices, reverse=reverse), "Ошибка сортировки цен"

    @allure.story("Сортировка по названию")
    @allure.title("Товары сортируются по названию: {sort_value}")
    @pytest.mark.catalog
    @pytest.mark.sorting
    @pytest.mark.parametrize(
        "sort_value, reverse",
        [
            ("az", False),
            ("za", True),
        ],
        ids=["name_a_to_z", "name_z_to_a"]
    )
    def test_sort_name(self, driver, logged_user, sort_value, reverse):
        with allure.step("Авторизоваться в системе"):
            inventory = logged_user()

        with allure.step(f"Выбрать сортировку '{sort_value}'"):
            inventory.sort_by(sort_value)

        with allure.step("Получить список названий товаров"):
            names = inventory.get_names()

        with allure.step("Проверить корректность сортировки названий"):
            assert names == sorted(names, reverse=reverse), "Ошибка сортировки названий"