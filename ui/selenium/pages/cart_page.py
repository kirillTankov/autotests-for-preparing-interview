from selenium.webdriver.common.by import By

from ui.selenium.pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.XPATH, '//span[@data-test="title"]')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def is_opened(self) -> bool:
        return self.find_visible_element(self.TITLE).text == 'Your Cart'

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def get_product_price(self, product_id):
        price_locator = (
            By.XPATH,
            f"//div[@class='cart_item'][.//button[@id='remove-{product_id}']]//div[@class='inventory_item_price']"
        )
        price_text = self.get_text(price_locator)
        return float(price_text.replace('$', '').strip())

    
