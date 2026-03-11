from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.XPATH, '//span[@data-test="title"]')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def is_opened(self) -> bool:
        return self.find_visible_element(self.TITLE).text == 'Your Cart'

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)