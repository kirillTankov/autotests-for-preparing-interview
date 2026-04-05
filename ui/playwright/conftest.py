import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.playwright)
        if "ui" not in item.keywords:
            item.add_marker(pytest.mark.ui)
