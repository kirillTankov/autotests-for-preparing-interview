from requests import Response

from api.clients.restful_booker.endpoints import RestfulBookerEndpoints
from api.clients.restful_booker.clients.base_client import BaseClient


class BookingClient(BaseClient):
    def get_booking_ids(self, **params) -> Response:
        return self.get(RestfulBookerEndpoints.BOOKING, params=params)

    def get_booking_by_id(self, booking_id: int) -> Response:
        return self.get(RestfulBookerEndpoints.booking_by_id(booking_id))

    def create_booking(self, payload: dict) -> Response:
        return self.post(RestfulBookerEndpoints.BOOKING, json=payload)

    def update_booking(self, booking_id: int, payload: dict, token: str) -> Response:
        headers = {
            "Cookie": f"token={token}"
        }
        return self.put(
            RestfulBookerEndpoints.booking_by_id(booking_id),
            json=payload,
            headers=headers
        )

    def delete_booking(self, booking_id: int, token: str):
        headers = {
            "Cookie": f'token={token}'
        }
        return self.delete(
            RestfulBookerEndpoints.booking_by_id(booking_id),
            headers=headers
        )
