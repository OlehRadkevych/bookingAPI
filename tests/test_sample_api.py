import os
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    client = APIClient(base_url="https://restful-booker.herokuapp.com")
    client.authenticate(auth_endpoint="/auth", username=os.environ.get('user'), password=os.environ.get('password'))
    return client

def test_get_request(api_client):
    response = api_client.get("/booking/1")
    assert response.status_code == 200