import pytest

from ui.playwright.pages.radio_button_page import RadioButtonPage

pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_select_yes_radio(page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open()

    radio_button_page.click_yes_radio()
    radio_button_page.should_have_yes_checked()
    radio_button_page.should_show_result_message()
    radio_button_page.should_show_selected_value("Yes")

def test_selected_impressive_radio(page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open()

    radio_button_page.click_impressive_radio()
    radio_button_page.should_have_impressive_radio()
    radio_button_page.should_show_result_message()
    radio_button_page.should_show_selected_value("Impressive")

def test_no_radio_disabled(page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open()

    radio_button_page.should_have_no_radio_disabled()