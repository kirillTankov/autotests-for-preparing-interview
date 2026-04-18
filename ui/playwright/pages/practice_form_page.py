from playwright.sync_api import Page

from ui.playwright.pages.base_page import BasePage


class PracticeFormPage(BasePage):
    PATH = "/automation-practice-form"

    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.mobile_input = page.locator("#userNumber")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.success_modal = page.locator(".modal-content")
        self.success_modal_title = page.locator("#example-modal-sizes-title-lg")

        self.gender_radio_buttons = {
            "Male": page.locator("label[for='gender-radio-1']"),
            "Female": page.locator("label[for='gender-radio-2']"),
            "Other": page.locator("label[for='gender-radio-3']"),
        }

    def fill_first_name(self, value: str):
        self.first_name_input.fill(value)

    def fill_last_name(self, value: str):
        self.last_name_input.fill(value)

    def fill_email(self, value: str):
        self.email_input.fill(value)

    def fill_mobile(self, value: str):
        self.mobile_input.fill(value)

    def select_gender(self, gender: str):
        try:
            self.gender_radio_buttons[gender].click()
        except KeyError:
            raise ValueError(f"Не поддерживаемое название \"gender\": {gender}")

    def submit(self):
        self.submit_button.click()

    def should_see_success_modal(self):
        self.should_be_visible(self.success_modal)

    def should_have_success_modal_title(self, title: str):
        self.should_have_text(self.success_modal_title, title)