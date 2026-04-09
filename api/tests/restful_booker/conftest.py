from typing import Generator

import pytest

from api.clients.restful_booker.clients.booking_client import BookingClient
from api.clients.restful_booker.test_data.auth_data import USERNAME, PASSWORD
from api.clients.restful_booker.clients.auth_client import AuthClient
from api.clients.restful_booker.test_data.booking_data import get_booking_payload


@pytest.fixture()
def auth_client() -> AuthClient:
    return AuthClient()


@pytest.fixture()
def booking_client() -> BookingClient:
    return BookingClient()


@pytest.fixture()
def auth_token(auth_client: AuthClient) -> str:
    response = auth_client.create_token(USERNAME, PASSWORD)

    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture()
def created_booking(
    booking_client: BookingClient,
    auth_token: str,
) -> Generator[int, None, None]:
    payload = get_booking_payload()

    response = booking_client.create_booking(payload=payload)
    assert response.status_code == 200

    booking_id = response.json()["bookingid"]

    yield booking_id

    delete_response = booking_client.delete_booking(booking_id, auth_token)
    assert delete_response.status_code in (200, 201)

