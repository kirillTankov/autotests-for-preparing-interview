import json
import allure
import pytest

from api.clients.restful_booker.test_data.booking_data import get_booking_payload, get_updated_booking_payload, \
    get_partial_update_booking_payload


@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Get booking ids")
@allure.title("GET /booking возвращает список идентификаторов бронирований")
@pytest.mark.api
@pytest.mark.api_restful_booker
def test_get_booking_ids(booking_client, created_booking):
    booking_id = created_booking

    with allure.step("Отправить GET-запрос на получение списка booking id"):
        response = booking_client.get_booking_ids()
        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("Проверить, что тело ответа имеет тип list и не пустое"):
        assert isinstance(data, list), "Тело ответа должно быть списком"
        assert len(data) > 0, "Список booking id не должен быть пустым"

    with allure.step(f"Проверить, что booking_id={booking_id} присутствует в списке"):
        actual_ids = [item["bookingid"] for item in data]
        assert booking_id in actual_ids, f"booking_id={booking_id} отсутствует в списке"

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Filter booking ids by firstname")
@allure.title("GET /booking с фильтром firstname возвращает подходящие бронирования")
@pytest.mark.api
@pytest.mark.api_restful_booker
def test_get_booking_ids_by_firstname(booking_client, created_booking):
    booking_id = created_booking
    firstname = "Autotester"

    with allure.step(f"Отправить GET-запрос на получение booking id с фильтром firstname={firstname}"):
        response = booking_client.get_booking_ids(firstname=firstname)
        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("Проверить, что тело ответа имеет тип list и не пустое"):
        assert isinstance(data, list), "Тело ответа должно быть списком"
        assert len(data) > 0, "Список booking id не должен быть пустым"

    with allure.step(f"Проверить, что booking_id={booking_id} присутствует в результате фильтрации"):
        actual_ids = [item["bookingid"] for item in data]
        assert booking_id in actual_ids, f"booking_id={booking_id} отсутствует в результате фильтрации"

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Get booking by id")
@allure.title("GET /booking/{id} возвращает бронирование по идентификатору")
@pytest.mark.api
@pytest.mark.api_restful_booker
def test_get_booking_by_id(booking_client, created_booking):
    booking_id = created_booking

    with allure.step(f"Отправить GET-запрос на получение booking_id={booking_id}"):
        response = booking_client.get_booking_by_id(booking_id)
        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("Проверить, что тело ответа имеет тип dict"):
        assert isinstance(data, dict), "Тело ответа должно быть объектом"

    with allure.step("Проверить основные поля бронирования"):
        assert data["firstname"] == "Autotester", "Некорректный firstname"
        assert data["lastname"] == "Autotest", "Некорректный lastname"
        assert data["totalprice"] == 228, "Некорректный totalprice"
        assert data["depositpaid"] is True, "Некорректный depositpaid"
        assert data["additionalneeds"] == "Breakfast", "Некорректный additionalneeds"

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Create booking")
@allure.title("POST /booking создает новое бронирование")
@pytest.mark.api
@pytest.mark.api_restful_booker
def test_post_create_booking(booking_client):
    payload = get_booking_payload()

    with allure.step("Подготовить payload для создания бронирования"):
        allure.attach(
            json.dumps(payload, indent=4, ensure_ascii=False),
            name="payload",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Отправить POST-запрос на создание бронирования"):
        response = booking_client.create_booking(payload=payload)
        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("Проверить, что ответ содержит bookingid типа int"):
        assert "bookingid" in data, "В ответе отсутствует bookingid"
        assert isinstance(data["bookingid"], int), "bookingid должен быть типа int"

    with allure.step("Проверить, что ответ содержит объект booking"):
        assert "booking" in data, "В ответе отсутствует объект booking"
        assert isinstance(data["booking"], dict), "Поле booking должно быть объектом"

    booking = data["booking"]

    with allure.step("Проверить, что данные созданного бронирования соответствуют payload"):
        assert booking["firstname"] == payload["firstname"], "Некорректный firstname"
        assert booking["lastname"] == payload["lastname"], "Некорректный lastname"
        assert booking["totalprice"] == payload["totalprice"], "Некорректный totalprice"
        assert booking["depositpaid"] is payload["depositpaid"], "Некорректный depositpaid"
        assert booking["additionalneeds"] == payload["additionalneeds"], "Некорректный additionalneeds"

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Update booking")
@allure.title("PUT /booking/{id} Обновить бронирование полностью")
@pytest.mark.api
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

    with allure.step("Проверить, что статус-код ответа равен 200"):
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

@allure.epic("API")
@allure.feature("Restful Booker")
@allure.story("Partial update booking")
@allure.title("PATCH /booking/{id} Обновить бронирование частично")
@pytest.mark.api
@pytest.mark.api_restful_booker
def test_patch_partial_update_booking(booking_client, created_booking, auth_token):
    booking_id = created_booking
    payload = get_partial_update_booking_payload()

    with allure.step(f"Подготовить payload для обновления booking id={booking_id}"):
        allure.attach(
            json.dumps(payload, indent=4, ensure_ascii=False),
            name="payload",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step(f"Отправить PATCH-запрос на обновление booking_id = {booking_id}"):
        response = booking_client.partial_update_booking(
            booking_id=booking_id,
            payload=payload,
            token=auth_token
        )
        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="response_body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
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
        assert data["firstname"] == payload["firstname"], "Некорректный firstname"
        assert data["lastname"] == payload["lastname"], "Некорректный lastname"