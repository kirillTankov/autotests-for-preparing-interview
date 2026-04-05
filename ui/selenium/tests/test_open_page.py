from ui.selenium.pages.example_page import ExamplePage


class TestExamplePage:
    def test_example_page(self, driver):
        example_page = ExamplePage(driver)
        example_page.open()
        example_page.check_opened()
