import pytest


@pytest.fixture(scope="session")
def base_url(request) -> str:
    return request.config.getoption("--ui-base-url")


@pytest.fixture(scope="session")
def wait_timeout(request) -> int:
    return int(request.config.getoption("--ui-wait"))
