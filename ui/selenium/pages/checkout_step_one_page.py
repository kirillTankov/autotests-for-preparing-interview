from selenium.webdriver.common.by import By

from ui.selenium.pages.base_page import BasePage


class CheckoutStepOne(BasePage):
    TITLE = (By.XPATH, '//span[@data-test="title"]')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_NAME = (By.ID, 'postal-code')
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    CONTINUE_BUTTON = (By.ID, 'continue')

    def is_opened(self) -> bool:
        return self.find_visible_element(self.TITLE).text == 'Checkout: Your Information'

    def fill_first_name(self, value):
        self.type_text(self.FIRST_NAME_FIELD, value, True)

    def fill_last_name(self, value):
        self.type_text(self.LAST_NAME_FIELD, value, True)

    def fill_postal_code(self, value):
        self.type_text(self.POSTAL_CODE_NAME, value, True)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def get_error_message(self) -> str:
        return self.find_visible_element(self.ERROR_MESSAGE).text
