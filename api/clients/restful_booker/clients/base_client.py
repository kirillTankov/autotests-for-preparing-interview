import requests

from config.config import RESTFUL_BOOKER_URL, TIMEOUT


class BaseClient:
    def __init__(self):
        self.base_url = RESTFUL_BOOKER_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        return self.session.post(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        return self.session.put(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def patch(self, endpoint, **kwargs):
        return self.session.patch(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )