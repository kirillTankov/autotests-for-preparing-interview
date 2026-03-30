from ui.pages.login_page import LoginPage


class TestLoginPage:
    def test_login_negative(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_field_username('locked_out_user')
        login_page.fill_field_password('secret_sauce')
        login_page.click_login_button()

        assert 'locked out' in login_page.get_error_text().lower()
