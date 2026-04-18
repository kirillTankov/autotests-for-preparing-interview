import pytest

from api.clients.restful_booker.test_data.auth_data import get_auth_data
from api.clients.restful_booker.schema import AuthResponse

pytestmark = [pytest.mark.api, pytest.mark.api_restful_booker]


def test_create_auth_token(auth_client):
    auth_data = get_auth_data()

    response = auth_client.create_token(auth_data)

    assert response.status_code == 200

    auth_response = AuthResponse.model_validate(response.json())

    assert auth_response.token
