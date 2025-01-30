import pytest
from utils.api_client import APIClient
from utils.booking import Booking


@pytest.fixture(scope="module")
def api_client():
    client = APIClient()
    client.authenticate()
    return client


@pytest.fixture(scope='function')
def booking() -> Booking:
    return Booking()
