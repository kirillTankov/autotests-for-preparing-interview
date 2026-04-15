from requests import Response

from api.clients.restful_booker.endpoints import RestfulBookerEndpoints
from api.clients.restful_booker.clients.base_client import BaseClient
from api.clients.restful_booker.schema import BookingData, PartialBookingData


class BookingClient(BaseClient):
    def get_booking_ids(self, **params) -> Response:
        return self.get(RestfulBookerEndpoints.BOOKING, params=params)

    def get_booking_by_id(self, booking_id: int) -> Response:
        return self.get(RestfulBookerEndpoints.booking_by_id(booking_id))

    def create_booking(self, payload: BookingData) -> Response:
        return self.post(RestfulBookerEndpoints.BOOKING, json=payload.model_dump(mode="json"))

    def update_booking(self, booking_id: int, payload: BookingData, token: str) -> Response:
        headers = {
            "Cookie": f"token={token}"
        }
        return self.put(
            RestfulBookerEndpoints.booking_by_id(booking_id),
            json=payload.model_dump(mode="json"),
            headers=headers
        )

    def partial_update_booking(self, booking_id: int, payload: PartialBookingData, token: str) -> Response:
        headers = {
            "Cookie": f"token={token}"
        }
        return self.patch(
            RestfulBookerEndpoints.booking_by_id(booking_id),
            json=payload.model_dump(mode="json", exclude_none=True),
            headers=headers
        )

    def delete_booking(self, booking_id: int, token: str):
        headers = {
            "Cookie": f"token={token}"
        }
        return self.delete(
            RestfulBookerEndpoints.booking_by_id(booking_id),
            headers=headers
        )
