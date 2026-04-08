from playwright.sync_api import expect

from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import expect


class PracticeFormPage(BasePage):
    PATH = "/automation-practice-form"
    FIRST_NAME_INPUT = "#firstName"
    LAST_NAME_INPUT = "#lastName"
    EMAIL_INPUT = "#userEmail"
    MOBILE_INPUT = "#userNumber"
    SUBMIT_BUTTON = "#submit"
    SUCCESS_MODAL = ".modal-content"
    SUCCESS_MODAL_TITLE = "#example-modal-sizes-title-lg"

    GENDER_SELECTORS = {
        "Male": 'label[for="gender-radio-1"]',
        "Female": 'label[for="gender-radio-2"]',
        "Other": 'label[for="gender-radio-3"]',
    }

    def fill_first_name(self, value: str):
        self.fill(self.FIRST_NAME_INPUT, value)

    def fill_last_name(self, value: str):
        self.fill(self.LAST_NAME_INPUT, value)

    def fill_email(self, value: str):
        self.fill(self.EMAIL_INPUT, value)

    def select_gender(self, gender: str):
        self.click(self.GENDER_SELECTORS[gender])

    def fill_mobile(self, value: str):
        self.fill(self.MOBILE_INPUT, value)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def should_see_success_modal(self):
        expect(self.page.locator(self.SUCCESS_MODAL)).to_be_visible()

    def should_have_success_modal_title(self, title: str):
        expect(self.page.locator(self.SUCCESS_MODAL_TITLE)).to_have_text(title)
