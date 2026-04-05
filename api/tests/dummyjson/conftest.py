import pytest

from api.clients.dummyjson.clients.products_client import ProductsClient


@pytest.fixture
def products_client():
    return ProductsClient()