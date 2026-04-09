import pytest

from ui.selenium.tests.artifacts.manager import save_failure_artifacts


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if not driver:
        return

    save_failure_artifacts(driver=driver, test_name=item.name)
