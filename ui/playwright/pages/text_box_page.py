from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import Page


class TextBoxPage(BasePage):
    PATH = "/text-box"

    def __init__(self, page: Page):
        super().__init__(page)

        self.full_name_input = page.get_by_placeholder("Full Name")
        self.email_input = page.locator("#userEmail")
        self.current_address = page.get_by_placeholder("Current Address")
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_button = page.get_by_role("button", name="Submit")

        self.name_output = page.locator("#name")
        self.email_output = page.locator("#email")
        self.current_address_output = page.locator("#output #currentAddress")
        self.permanent_address_output = page.locator("#output #permanentAddress")

    def fill_full_name(self, value: str):
        self.full_name_input.fill(value)

    def fill_email(self, value: str):
        self.email_input.fill(value)

    def fill_current_address(self, value: str):
        self.current_address.fill(value)

    def fill_permanent_address(self, value: str):
        self.permanent_address.fill(value)

    def submit(self):
        self.submit_button.click()

    def should_have_submitted_name(self, value: str):
        self.should_have_text(self.name_output, f"Name:{value}")

    def should_have_submitted_email(self, value: str):
        self.should_have_text(self.email_output, f"Email:{value}")

    def should_have_submitted_current_address(self, value: str):
        self.should_have_text(self.current_address_output, f"Current Address :{value}")

    def should_have_submitted_permanent_address(self, value: str):
        self.should_have_text(self.permanent_address_output, f"Permananet Address :{value}")