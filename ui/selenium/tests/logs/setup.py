import logging

from ui.selenium.tests.utils.paths import LOGS_DIR


def configure_project_logging() -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("ui_tests")
    if logger.handlers:
        return

    log_file = LOGS_DIR / "ui-tests.log"
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.propagate = False
