from api.clients.restful_booker.schema import AuthData

def get_auth_data() -> AuthData:
    return AuthData(
        username="admin",
        password="password123"
    )