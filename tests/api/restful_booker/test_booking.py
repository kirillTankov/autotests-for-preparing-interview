import json

import allure
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

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Update booking")
@allure.title("Обновить существующее бронирование")
@pytest.mark.api_restful_booker
def test_put_update_booking(booking_client, created_booking, auth_token):
    payload = get_updated_booking_payload()

    with allure.step(f"Подготовить payload для обновления booking id={created_booking}"):
        allure.attach(
            json.dumps(payload, indent=4, ensure_ascii=False),
            name="payload",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step(f"Отправить PUT-запрос на обновление booking id={created_booking}"):
        response = booking_client.update_booking(
            created_booking,
            payload=payload,
            token=auth_token
        )

    allure.attach(
        json.dumps(response.json(), indent=4, ensure_ascii=False),
        name="response_body",
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step("Проверить статус-код ответа"):
        allure.attach(
            str(response.status_code),
            name=f"status_code: {response.status_code}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 200

    data = response.json()

    with allure.step("Проверить, что тело ответа имеет тип dict"):
        assert isinstance(data, dict)

    with allure.step("Проверить основные поля бронирования"):
        assert data["firstname"] == payload["firstname"]
        assert data["lastname"] == payload["lastname"], "Некорректный lastname"
        assert data["totalprice"] == payload["totalprice"], "Некорректный totalprice"
        assert data["depositpaid"] is payload["depositpaid"], "Некорректный depositpaid"
        assert data["additionalneeds"] == payload["additionalneeds"], "Некорректный additionalneeds"

    with allure.step("Проверить даты бронирования"):
        assert data["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
        assert data["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]