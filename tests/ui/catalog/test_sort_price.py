import pytest


class TestSortPrice:

    @pytest.mark.catalog
    @pytest.mark.sorting
    @pytest.mark.parametrize(
        'sort_value, reverse',
        [
            ('lohi', False),
            ('hilo', True)
        ],
        ids=["price_low_to_high", "price_high_to_low"]
    )
    def test_sort_price(self, driver, logged_user, sort_value, reverse):
        inventory = logged_user()

        inventory.sort_by(sort_value)
        prices = inventory.get_prices()

        assert prices == sorted(prices, reverse=reverse), 'Ошибка цен'


    @pytest.mark.catalog
    @pytest.mark.sorting
    @pytest.mark.parametrize(
        'sort_value, reverse',
        [
            ('az', False),
            ('za', True)
        ],
        ids=["name_a_to_z", "name_z_to_a"]
    )
    def test_sort_name(self, driver, logged_user, sort_value, reverse):
        inventory = logged_user()

        inventory.sort_by(sort_value)
        names = inventory.get_names()

        assert names == sorted(names, reverse=reverse)
