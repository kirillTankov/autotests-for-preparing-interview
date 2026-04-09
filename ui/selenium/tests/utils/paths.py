from pathlib import Path

LOGS_DIR = Path("logs")
ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
PAGE_SOURCE_DIR = ARTIFACTS_DIR / "page_source"


def ensure_runtime_directories() -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_SOURCE_DIR.mkdir(parents=True, exist_ok=True)
