import pytest

from ui.playwright.pages.text_box_page import TextBoxPage


pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_submit_text_box_with_valid_data(page):
    text_box_page = TextBoxPage(page)
    text_box_page.open()

    text_box_page.fill_full_name("Test Full Name")
    text_box_page.fill_email("etest_my_mail@gmail.com")
    text_box_page.fill_current_address("Current   address")
    text_box_page.fill_permanent_address("eper sd as   ")
    text_box_page.submit()

    text_box_page.should_have_submitted_name("Test Full Name")
    text_box_page.should_have_submitted_email("etest_my_mail@gmail.com")
    text_box_page.should_have_submitted_current_address("Current   address")
    text_box_page.should_have_submitted_permanent_address("eper sd as   ")