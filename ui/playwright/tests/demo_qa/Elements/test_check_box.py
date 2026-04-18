import pytest

from ui.playwright.pages.check_box_page import CheckBoxPage


pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_select_react_checkbox_and_show_selected_result(page):
    check_box_page = CheckBoxPage(page)
    check_box_page.open()

    check_box_page.expand_home()
    check_box_page.expand_documents()
    check_box_page.expand_workspace()
    check_box_page.select_react_checkbox()

    check_box_page.should_see_result_block()
    check_box_page.should_have_selected_item("react")