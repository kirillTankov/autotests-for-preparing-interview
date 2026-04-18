from playwright.sync_api import Page, Locator, expect
from ui.playwright.config.settings import Settings


class BasePage:
    PATH = ""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = Settings.BASE_URL.rstrip("/")

    def open(self):
        url = f"{self.base_url}/{self.PATH.lstrip('/')}" if self.PATH else self.base_url
        self.page.goto(url)

    def should_have_title(self, title: str):
        expect(self.page).to_have_title(title)

    def should_have_url(self, url_or_path: str):
        expected_url = (
            f"{self.base_url}/{url_or_path.lstrip('/')}"
            if not url_or_path.startswith("http")
            else url_or_path
        )
        expect(self.page).to_have_url(expected_url)

    @staticmethod
    def should_be_visible(locator: Locator):
        expect(locator).to_be_visible()

    @staticmethod
    def should_not_be_visible(locator: Locator):
        expect(locator).not_to_be_visible()

    @staticmethod
    def should_be_checked(locator: Locator):
        expect(locator).to_be_checked()

    @staticmethod
    def should_have_text(locator: Locator, text: str):
        expect(locator).to_have_text(text)

    @staticmethod
    def should_contain_text(locator: Locator, text: str):
        expect(locator).to_contain_text(text)

    @staticmethod
    def should_have_value(locator: Locator, value: str):
        expect(locator).to_have_value(value)

    @staticmethod
    def should_be_enabled(locator: Locator):
        expect(locator).to_be_enabled()

    @staticmethod
    def should_be_disabled(locator: Locator):
        expect(locator).to_be_disabled()

    @staticmethod
    def should_have_attribute(locator: Locator, name: str, value: str):
        expect(locator).to_have_attribute(name, value)