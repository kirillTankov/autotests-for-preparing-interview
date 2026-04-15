from api.clients.restful_booker.clients.base_client import BaseClient
from api.clients.restful_booker.endpoints import RestfulBookerEndpoints
from api.clients.restful_booker.schema import AuthData


class AuthClient(BaseClient):
    def create_token(self, auth_data: AuthData):
        return self.post(
            RestfulBookerEndpoints.AUTH,
            json=auth_data.model_dump(mode="json"),
        )