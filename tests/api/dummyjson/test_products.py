import pytest


@pytest.mark.api_dummy_json
def test_get_all_products(products_client):
    response = products_client.get_all_products()

    assert response.status_code == 200

    body = response.json()

    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) > 0

@pytest.mark.api_dummy_json
def test_get_product_by_id(products_client):
    response = products_client.get_products_by_id(product_id=1)

    assert response.status_code == 200

    body = response.json()

    assert body['id'] == 1
    assert 'title' in body

@pytest.mark.api_dummy_json
def test_search_products(products_client):
    response = products_client.get_search_products(query='phone')

    assert response.status_code == 200

    body = response.json()

    assert len(body['products']) > 0
    assert isinstance(body['products'], list)
    assert 'products' in body
    assert 'title' in body['products'][0]

@pytest.mark.api_dummy_json
def test_create_product(products_client):
    payload = {
        "title": "Моя тачка",
        "price": 777
    }

    response = products_client.create_product(body=payload)

    assert response.status_code == 201

    body = response.json()

    assert body['title'] == payload['title']
    assert body['price'] == payload['price']

@pytest.mark.api_dummy_json
def test_update_product(products_client):
    payload = {
        "title": "Updated products",
        "price": 555
    }

    response = products_client.update_product(product_id=1, body=payload)

    assert response.status_code == 200

    body = response.json()

    assert body['id'] == 1
    assert body['title'] == payload['title']
    assert body['price'] == payload['price']

@pytest.mark.api_dummy_json
def test_patch_product(products_client):
    payload = {
        "title": "Patched title"
    }

    response = products_client.patch_product(product_id=1, body=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["title"] == payload["title"]

@pytest.mark.api_dummy_json
def test_delete_product(products_client):
    response = products_client.delete_product(product_id=1)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1