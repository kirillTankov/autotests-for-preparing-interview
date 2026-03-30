from ui.pages.base_page import BasePage


class ExamplePage(BasePage):
    URL = 'https://example.com'

    def open(self):
        self.driver.get(self.URL)

    def check_opened(self):
        assert 'Example Domain' in self.driver.title

