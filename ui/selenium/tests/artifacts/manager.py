import allure
from selenium.webdriver.remote.webdriver import WebDriver

from ui.selenium.tests.utils.naming import sanitize_test_name, timestamp_for_filename
from ui.selenium.tests.utils.paths import PAGE_SOURCE_DIR, SCREENSHOTS_DIR


def save_failure_artifacts(driver: WebDriver, test_name: str) -> None:
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = timestamp_for_filename()
    safe_test_name = sanitize_test_name(test_name)

    screenshot_path = SCREENSHOTS_DIR / f"{safe_test_name}_{timestamp}.png"
    page_source_path = PAGE_SOURCE_DIR / f"{safe_test_name}_{timestamp}.html"

    try:
        driver.save_screenshot(str(screenshot_path))
        allure.attach.file(
            str(screenshot_path),
            name=f"{safe_test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass

    try:
        page_source = driver.page_source
        page_source_path.write_text(page_source, encoding="utf-8")
        allure.attach(
            page_source,
            name=f"{safe_test_name}_page_source",
            attachment_type=allure.attachment_type.HTML,
        )
    except Exception:
        pass
