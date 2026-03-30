from api.clients.restful_booker.clients.base_client import BaseClient
from api.clients.restful_booker.endpoints import RestfulBookerEndpoints


class AuthClient(BaseClient):
    def create_token(self, username: str, password: str):
        payload = {
            "username": username,
            "password": password
        }
        return self.post(f'{RestfulBookerEndpoints.AUTH}', json=payload)