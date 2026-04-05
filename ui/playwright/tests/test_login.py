from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    username_field = page.get_by_label("Username")
    password_field = page.get_by_label("Password")
    login_button = page.get_by_role("button", name="Submit")

    username_field.fill("student")
    password_field.fill("Password123")
    login_button.click()

    log_out_button = page.get_by_role("link", name="Log out")

    expect(page).to_have_title("Logged In Successfully | Practice Test Automation")
    expect(log_out_button).to_have_text("Log out")
    expect(log_out_button).to_be_visible()