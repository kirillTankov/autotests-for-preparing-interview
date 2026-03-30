from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'

    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_TEXT = (By.XPATH, '//h3[@data-test="error"]')

    def open(self):
        self.driver.get(self.URL)

    def fill_field_username(self, username: str):
        self.type_text(self.USERNAME, username)

    def fill_field_password(self, password: str):
        self.type_text(self.PASSWORD, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_error_text(self):
        return self.find_visible_element(self.ERROR_TEXT).text

    def login_as(self, username, password):
        self.fill_field_username(username)
        self.fill_field_password(password)
        self.click_login_button()