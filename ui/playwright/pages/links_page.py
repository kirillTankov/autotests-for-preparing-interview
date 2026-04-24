from playwright.sync_api import Page, expect
from ui.playwright.pages.base_page import BasePage


class LinksPage(BasePage):
    PATH = "/links"

    def __init__(self, page: Page):
        super().__init__(page)
        self.new_tab = None

        self.home_link = page.get_by_role("link", name="Home", exact=True)
        self.dynamic_home_link = page.locator("#dynamicLink")

        self.created_link = page.get_by_role("link", name="Created", exact=True)
        self.no_content_link = page.get_by_role("link", name="No Content", exact=True)
        self.moved_link = page.get_by_role("link", name="Moved", exact=True)
        self.bad_request_link = page.get_by_role("link", name="Bad Request", exact=True)
        self.unauthorized_link = page.get_by_role("link", name="Unauthorized", exact=True)
        self.forbidden_link = page.get_by_role("link", name="Forbidden", exact=True)
        self.not_found_link = page.get_by_role("link", name="Not Found", exact=True)

        self.response_link = page.locator("#linkResponse")

    def click_home_link_and_get_new_tab(self):
        with self.page.expect_popup() as popup_info:
            self.home_link.click()
        self.new_tab = popup_info.value

    def click_dynamic_home_link_and_get_new_tab(self):
        with self.page.expect_popup() as popup_info:
            self.dynamic_home_link.click()
        self.new_tab = popup_info.value

    def should_have_new_tab_url(self, url: str):
        expect(self.new_tab).to_have_url(url)

    def click_response_link(self, link_name: str):
        self.page.get_by_role("link", name=link_name, exact=True).click()

    def should_have_response(self, status_code: str, status_text: str):
        self.should_contain_text(self.response_link, status_code)
        self.should_contain_text(self.response_link, status_text)