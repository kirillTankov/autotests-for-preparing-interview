import pytest

from api.clients.restful_booker.test_data.auth_data import get_auth_data

pytestmark = [pytest.mark.api, pytest.mark.api_restful_booker]


def test_create_auth_token(auth_client):
    auth_data = get_auth_data()

    response = auth_client.create_token(auth_data)
    body = response.json()

    assert response.status_code == 200
    assert "token" in body
    assert isinstance(body["token"], str)