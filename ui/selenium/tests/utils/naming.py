from datetime import datetime


def timestamp_for_filename() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def sanitize_test_name(test_name: str) -> str:
    return test_name.replace("/", "_").replace("\\", "_").replace(":", "_")
