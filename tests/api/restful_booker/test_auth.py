import pytest

from api.clients.restful_booker.test_data.auth_data import USERNAME, PASSWORD


@pytest.mark.api
@pytest.mark.api_restful_booker
def test_create_auth_token(auth_client):
    response = auth_client.create_token(USERNAME, PASSWORD)

    assert response.status_code == 200
    assert 'token' in response.json()
    assert isinstance(response.json()['token'], str)