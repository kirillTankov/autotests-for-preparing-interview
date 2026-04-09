import pytest

from ui.playwright.pages.practice_form_page import PracticeFormPage


pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_submit_practice_form(page):
    practice_form_page = PracticeFormPage(page)

    practice_form_page.open()
    practice_form_page.fill_first_name("Ivan")
    practice_form_page.fill_last_name("Petrov")
    practice_form_page.fill_email("ivan@example.com")
    practice_form_page.select_gender("Male")
    practice_form_page.fill_mobile("9998887766")
    practice_form_page.submit()

    practice_form_page.should_see_success_modal()
    practice_form_page.should_have_success_modal_title("Thanks for submitting the form")
