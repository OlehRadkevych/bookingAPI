import requests
from config import Config

config = Config()


class APIClient:
    def __init__(self, base_url=config.BASE_URL, username=config.USERNAME, password=config.PASSWORD):
        self.base_url = base_url
        self.auth_endpoint = '/auth'
        self.username = username
        self.password = password
        self.auth_token = None

    def authenticate(self):
        response = requests.post(f"{self.base_url}{self.auth_endpoint}",
                                 json={"username": self.username, "password": self.password})
        if response.status_code == 200:
            self.auth_token = response.json().get("token")
        else:
            raise Exception(f"Authentication failed: {response.status_code}, {response.text}")

    def _get_headers(self, headers):
        default_headers = {
            "Authorization": f"Bearer {self.auth_token}" if self.auth_token else None,
            "Content-Type": "application/json"
        }
        if headers:
            default_headers.update(headers)
        return {k: v for k, v in default_headers.items() if v is not None}

    def get(self, endpoint, headers=None, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self._get_headers(headers), params=params)
        return response

    def post(self, endpoint, headers=None, data=None, json=None):
        response = requests.post(f"{self.base_url}{endpoint}", headers=self._get_headers(headers), data=data, json=json)
        return response

    def put(self, endpoint, headers=None, data=None, json=None):
        response = requests.put(f"{self.base_url}{endpoint}", headers=self._get_headers(headers), data=data, json=json)
        return response

    def patch(self, endpoint, headers=None, data=None, json=None):
        response = requests.patch(f"{self.base_url}{endpoint}", headers=self._get_headers(headers), data=data,
                                  json=json)
        return response

    def delete(self, endpoint, headers=None):
        response = requests.delete(f"{self.base_url}{endpoint}", headers=self._get_headers(headers))
        return response
