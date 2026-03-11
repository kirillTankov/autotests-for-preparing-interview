from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.XPATH, '//span[@data-test="title"]')
    ITEMS = (By.CLASS_NAME, 'inventory_item')
    SORT_SELECT = (By.CLASS_NAME, 'product_sort_container')
    PRICES = (By.CLASS_NAME, 'inventory_item_price')
    BURGER_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    BURGER_MENU_PANEL = (By.CLASS_NAME, 'bm-menu-wrap')
    BURGER_MENU_CLOSE_BUTTON = (By.ID, 'react-burger-cross-btn')
    ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_CONTAINER = (By.ID, 'shopping_cart_container')

    def is_opened(self) -> bool:
        return self.find_visible_element(self.TITLE).text == 'Products'

    def items_count(self) -> int:
        return len(self.driver.find_elements(*self.ITEMS))

    def select_sort(self, value: str):
        el = self.find_visible_element(self.SORT_SELECT)
        Select(el).select_by_value(value)

    def get_prices(self) -> list[float]:
        prices_els = self.driver.find_elements(*self.PRICES)
        return [float(el.text.replace('$', '').strip()) for el in prices_els]

    def get_names(self) -> list[str]:
        items = self.find_elements(self.ITEM_NAMES)
        return [item.text for item in items]

    def wait_prices_changed(self, old_prices: list[float]):
        self.wait.until(lambda d: self.get_prices() != old_prices)

    def sort_by(self, value: str):
        # old_prices = self.get_prices()
        self.select_sort(value)
        # self.wait_prices_changed(old_prices)
        return self

    def open_menu(self):
        self.click_element(self.BURGER_MENU_BUTTON)
        self.wait_text_in_attribute(self.BURGER_MENU_PANEL, 'aria-hidden', 'false')
        self.wait_clickable(self.BURGER_MENU_CLOSE_BUTTON)

    def is_burger_menu_open(self) -> bool:
        aria_hidden = self.get_attribute(self.BURGER_MENU_PANEL, "aria-hidden")
        return aria_hidden == 'false'

    def close_menu(self):
        for _ in range(3):
            try:
                close_btn = self.wait_clickable(self.BURGER_MENU_CLOSE_BUTTON)
                ActionChains(self.driver).move_to_element(close_btn).click(close_btn).perform()
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                self.wait.until(lambda d: True)

        self.wait_text_in_attribute(self.BURGER_MENU_PANEL, "aria-hidden", "true")

    def add_to_cart(self, product_id: str):
        add_button = (By.ID, f"add-to-cart-{product_id}")
        remove_button = (By.ID, f'remove-{product_id}')

        self.click_element(add_button)
        self.wait_present(remove_button)

    def is_product_added(self, product_id: str) -> bool:
        remove_button = (By.ID, f"remove-{product_id}")
        return self.is_element_present(remove_button)

    def get_cart_badge_text(self) -> str:
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click_element(self.CART_CONTAINER)
