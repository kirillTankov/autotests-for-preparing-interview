import json
from typing import TypeVar

import allure
import pytest
from pydantic import BaseModel

from api.clients.restful_booker.schema import (
    BookingData,
    BookingIdItem,
    BookingResponse,
    CreateBookingResponse,
    PartialBookingData,
)
from api.clients.restful_booker.test_data.booking_data import (
    get_booking_payload,
    get_partial_update_booking_payload,
    get_updated_booking_payload,
)

pytestmark = [pytest.mark.api, pytest.mark.api_restful_booker]

ModelT = TypeVar("ModelT", bound=BaseModel)


def _attach_json(name: str, payload) -> None:
    if isinstance(payload, BaseModel):
        payload = payload.model_dump(mode="json", exclude_none=True)

    allure.attach(
        json.dumps(payload, indent=4, ensure_ascii=False),
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )


def _parse_response(response, model: type[ModelT]) -> ModelT:
    body = response.json()
    _attach_json("response_body", body)
    return model.model_validate(body)


def _parse_response_list(response, model: type[ModelT]) -> list[ModelT]:
    body = response.json()
    _attach_json("response_body", body)
    return [model.model_validate(item) for item in body]


def _assert_booking_fields(actual: BookingResponse, expected: BookingData) -> None:
    assert actual.firstname == expected.firstname
    assert actual.lastname == expected.lastname
    assert actual.totalprice == expected.totalprice
    assert actual.depositpaid == expected.depositpaid
    assert actual.additionalneeds == expected.additionalneeds
    assert actual.bookingdates.checkin == expected.bookingdates.checkin
    assert actual.bookingdates.checkout == expected.bookingdates.checkout


def _assert_partial_booking_fields(actual: BookingResponse, expected: PartialBookingData) -> None:
    if expected.firstname is not None:
        assert actual.firstname == expected.firstname
    if expected.lastname is not None:
        assert actual.lastname == expected.lastname


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Get booking ids")
@allure.title("GET /booking returns booking ids")
def test_get_booking_ids(booking_client, created_booking):
    response = booking_client.get_booking_ids()

    assert response.status_code == 200

    booking_items = _parse_response_list(response, BookingIdItem)

    assert booking_items
    assert created_booking in [item.bookingid for item in booking_items]


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Filter booking ids by firstname")
@allure.title("GET /booking with firstname filter returns matching bookings")
def test_get_booking_ids_by_firstname(booking_client, created_booking):
    firstname = get_booking_payload().firstname

    response = booking_client.get_booking_ids(firstname=firstname)

    assert response.status_code == 200

    booking_items = _parse_response_list(response, BookingIdItem)

    assert booking_items
    assert created_booking in [item.bookingid for item in booking_items]


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Get booking by id")
@allure.title("GET /booking/{id} returns booking data")
def test_get_booking_by_id(booking_client, created_booking):
    expected_booking = get_booking_payload()

    response = booking_client.get_booking_by_id(created_booking)

    assert response.status_code == 200

    actual_booking = _parse_response(response, BookingResponse)

    _assert_booking_fields(actual_booking, expected_booking)


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Create booking")
@allure.title("POST /booking creates a new booking")
def test_post_create_booking(booking_client):
    payload = get_booking_payload()
    _attach_json("payload", payload)

    response = booking_client.create_booking(payload=payload)

    assert response.status_code == 200

    created_booking = _parse_response(response, CreateBookingResponse)

    assert created_booking.bookingid > 0
    _assert_booking_fields(created_booking.booking, payload)


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Update booking")
@allure.title("PUT /booking/{id} fully updates booking")
def test_put_update_booking(booking_client, created_booking, auth_token):
    payload = get_updated_booking_payload()
    _attach_json("payload", payload)

    response = booking_client.update_booking(created_booking, payload=payload, token=auth_token)

    assert response.status_code == 200

    updated_booking = _parse_response(response, BookingResponse)

    _assert_booking_fields(updated_booking, payload)


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Partial update booking")
@allure.title("PATCH /booking/{id} partially updates booking")
def test_patch_partial_update_booking(booking_client, created_booking, auth_token):
    payload = get_partial_update_booking_payload()
    _attach_json("payload", payload)

    response = booking_client.partial_update_booking(
        booking_id=created_booking,
        payload=payload,
        token=auth_token,
    )

    assert response.status_code == 200

    updated_booking = _parse_response(response, BookingResponse)

    _assert_partial_booking_fields(updated_booking, payload)
