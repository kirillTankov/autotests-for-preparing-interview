from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import Page


class ButtonsPage(BasePage):
    PATH = "/buttons"

    def __init__(self, page: Page):
        super().__init__(page)

        self.double_click_button = page.get_by_role("button", name="Double Click Me", exact=True)
        self.right_click_button = page.get_by_role("button", name="Right Click Me", exact=True)
        self.click_me_button  = page.get_by_role("button", name="Click Me", exact=True)

        self.double_click_message = page.locator("#doubleClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.dynamic_click_message  = page.locator("#dynamicClickMessage")

    def double_click(self):
        self.double_click_button.dblclick()

    def right_click(self):
        self.right_click_button.click(button="right")

    def click_me(self):
        self.click_me_button.click()

    def should_have_double_message(self):
        self.should_have_text(self.double_click_message, "You have done a double click")

    def should_have_right_message(self):
        self.should_have_text(self.right_click_message, "You have done a right click")

    def should_have_dynamic_message(self):
        self.should_have_text(self.dynamic_click_message, "You have done a dynamic click")
