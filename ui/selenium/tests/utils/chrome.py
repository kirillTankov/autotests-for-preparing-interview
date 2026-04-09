from selenium.webdriver.chrome.options import Options


def build_chrome_options(headed: bool = False) -> Options:
    options = Options()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=PasswordManagerEnabled,PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")

    if headed:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    return options
