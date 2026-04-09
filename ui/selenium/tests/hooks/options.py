import os


def pytest_addoption(parser):
    parser.addoption(
        "--ui-base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://www.saucedemo.com/"),
        help="Base UI application URL",
    )
    parser.addoption(
        "--ui-wait",
        action="store",
        default=os.getenv("WAIT_TIMEOUT", "10"),
        help="UI explicit wait timeout in seconds",
    )
    parser.addoption(
        "--ui-headed",
        action="store_true",
        default=os.getenv("HEADED", "false").lower() == "true",
        help="Run browser in headed mode",
    )
