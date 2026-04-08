from playwright.sync_api import Page, expect

from ui.playwright.config.settings import Settings


class BasePage:
    PATH = ""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = Settings.BASE_URL.rstrip("/")

    def open(self):
        url = f"{self.base_url}/{self.PATH.lstrip('/')}" if self.PATH else self.base_url
        self.page.goto(url)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_visible(self, selector: str):
        self.page.locator(selector).wait_for(state="visible")

    def wait_hidden(self, selector: str):
        self.page.locator(selector).wait_for(state="hidden")

    def should_have_title(self, title: str):
        expect(self.page).to_have_title(title)

    def should_have_url(self, url_or_path: str):
        expected_url = (
            f"{self.base_url}/{url_or_path.lstrip('/')}"
            if not url_or_path.startswith("http")
            else url_or_path
        )
        expect(self.page).to_have_url(expected_url)

