import pytest

from ui.playwright.pages.buttons_page import ButtonsPage

pytestmark = [pytest.mark.ui, pytest.mark.playwright]



def test_buttons(page):
    buttons_page = ButtonsPage(page)
    buttons_page.open()

    buttons_page.double_click()
    buttons_page.should_have_double_message()

    buttons_page.right_click()
    buttons_page.should_have_right_message()

    buttons_page.click_me()
    buttons_page.should_have_dynamic_message()