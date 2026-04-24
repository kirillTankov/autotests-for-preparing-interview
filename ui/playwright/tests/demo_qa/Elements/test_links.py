import pytest

from ui.playwright.pages.links_page import LinksPage


pytestmark = [pytest.mark.ui, pytest.mark.playwright]


def test_home_link_opens_new_tab(page):
    links_page = LinksPage(page)
    links_page.open()

    links_page.click_home_link_and_get_new_tab()
    links_page.should_have_new_tab_url("https://demoqa.com/")

def test_dynamic_home_link_opens_new_tab(page):
    links_page = LinksPage(page)
    links_page.open()

    links_page.click_dynamic_home_link_and_get_new_tab()
    links_page.should_have_new_tab_url("https://demoqa.com/")

@pytest.mark.parametrize(
    "link_name,status_code,status_text",
    [
        ("Created", "201", "Created"),
        ("No Content", "204", "No Content"),
        ("Moved", "301", "Moved Permanently"),
        ("Bad Request", "400", "Bad Request"),
        ("Unauthorized", "401", "Unauthorized"),
        ("Forbidden", "403", "Forbidden"),
        ("Not Found", "404", "Not Found"),
    ],
)
def test_links_response(page, link_name, status_code, status_text):
    links_page = LinksPage(page)
    links_page.open()

    links_page.click_response_link(link_name)
    links_page.should_have_response(status_code, status_text)

