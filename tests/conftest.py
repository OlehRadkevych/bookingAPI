import pytest
from utils.api_client import APIClient
from config import BASE_URL, USER_NAME, PASSWORD


@pytest.fixture(scope="module")
def api_client():
    client = APIClient(base_url=BASE_URL, username=USER_NAME, password=PASSWORD)
    client.authenticate()
    return client
