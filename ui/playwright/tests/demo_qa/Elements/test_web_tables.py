import pytest

from ui.playwright.pages.web_tables_page import WebTablesPage

pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_add_new_user_in_table(page):
    web_tables_page = WebTablesPage(page)
    web_tables_page.open()

    web_tables_page.add_user(
        first_name="Ivan",
        last_name="Petrov",
        age="25",
        email="ivan.petrov.qa@example.com",
        salary="5000",
        department="QA",
    )

    web_tables_page.should_have_user_in_table(
        first_name="Ivan",
        last_name="Petrov",
        age="25",
        email="ivan.petrov.qa@example.com",
        salary="5000",
        department="QA",
    )
