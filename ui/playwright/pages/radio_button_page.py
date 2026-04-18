from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import Page


class RadioButtonPage(BasePage):
    PATH = "/radio-button"

    def __init__(self, page: Page):
        super().__init__(page)

        self.yes_radio = page.get_by_role("radio", name="Yes")
        self.impressive_radio = page.get_by_role("radio", name="Impressive")
        self.no_radio = page.get_by_role("radio", name="No")

        self.result_text = page.locator("p.mt-3")
        self.success_text = page.locator(".text-success")


    def click_yes_radio(self):
        self.yes_radio.check()

    def click_impressive_radio(self):
        self.impressive_radio.check()

    def should_show_result_message(self):
        self.should_contain_text(self.result_text, "You have selected")

    def should_show_selected_value(self, value: str):
        self.should_have_text(self.success_text, value)

    def should_have_no_radio_disabled(self):
        self.should_be_disabled(self.no_radio)

    def should_have_yes_checked(self):
        self.should_be_checked(self.yes_radio)

    def should_have_impressive_radio(self):
        self.should_be_checked(self.impressive_radio)