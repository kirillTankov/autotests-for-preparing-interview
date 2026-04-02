from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible_element(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_presense_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple, text: str, clear: bool = True):
        el = self.find_visible_element(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_text(self, locator: tuple) -> str:
        return self.find_visible_element(locator).text

    def get_attribute(self, locator: tuple, name: str) -> str:
        return self.find_presense_element(locator).get_attribute(name)

    def wait_invisible(self, locator: tuple):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_present(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_text_in_attribute(self, locator: tuple, attr: str, text: str):
        return self.wait.until(EC.text_to_be_present_in_element_attribute(locator, attr, text))

    def is_element_present(self, locator: tuple) -> bool:
        return len(self.driver.find_elements(*locator)) > 0