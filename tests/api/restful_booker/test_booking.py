import pytest

from api.clients.restful_booker.test_data.booking_data import get_booking_payload, get_updated_booking_payload


@pytest.mark.api_restful_booker
def test_get_booking_ids(booking_client, created_booking):
    response = booking_client.get_booking_ids()

    assert response.status_code == 200

    booking_ids = response.json()
    actual_ids = [item["bookingid"] for item in booking_ids]

    assert created_booking in actual_ids

    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.api_restful_booker
def test_get_booking_ids_by_firstname(booking_client, created_booking):
    response = booking_client.get_booking_ids(firstname='Autotester')

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    actual_ids = [item["bookingid"] for item in data]

    assert created_booking in actual_ids

@pytest.mark.api_restful_booker
def test_get_booking_by_id(booking_client, created_booking):
    response = booking_client.get_booking_by_id(created_booking)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["firstname"] == "Autotester", "Некорректный firstname"
    assert data["lastname"] == "Autotest", "Некорректный lastname"
    assert data["totalprice"] == 228, "Некорректный totalprice"
    assert data["depositpaid"] is True, "Некорректный depositpaid"
    assert data["additionalneeds"] == "Breakfast", "Некорректный additionalneeds"

@pytest.mark.api_restful_booker
def test_post_create_booking(booking_client):
    payload = get_booking_payload()

    response = booking_client.create_booking(payload=payload)

    assert response.status_code == 200

    data = response.json()

    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)

    booking = data["booking"]

    assert booking["firstname"] == payload["firstname"], "Некорректный firstname"
    assert booking["lastname"] == payload["lastname"], "Некорректный lastname"
    assert booking["totalprice"] == payload["totalprice"], "Некорректный totalprice"
    assert booking["depositpaid"] is payload["depositpaid"], "Некорректный depositpaid"
    assert booking["additionalneeds"] == payload["additionalneeds"], "Некорректный additionalneeds"

@pytest.mark.api_restful_booker
def test_put_update_booking(booking_client, created_booking, auth_token):
    payload = get_updated_booking_payload()

    response = booking_client.update_booking(
        created_booking,
        payload=payload,
        token=auth_token
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["firstname"] == payload["firstname"]
    assert data["lastname"] == payload["lastname"], "Некорректный lastname"
    assert data["totalprice"] == payload["totalprice"], "Некорректный totalprice"
    assert data["depositpaid"] is payload["depositpaid"], "Некорректный depositpaid"
    assert data["additionalneeds"] == payload["additionalneeds"], "Некорректный additionalneeds"
    assert data["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert data["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
