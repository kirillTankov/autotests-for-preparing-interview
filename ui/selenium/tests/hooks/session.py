from ui.selenium.tests.logs.setup import configure_project_logging
from ui.selenium.tests.utils.paths import ensure_runtime_directories


def pytest_sessionstart(session):
    del session
    ensure_runtime_directories()
    configure_project_logging()
