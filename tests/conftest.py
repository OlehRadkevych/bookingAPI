import pytest
from utils.api_client import APIClient
from utils.booking import Booking
import datetime


@pytest.fixture(scope="module")
def api_client():
    client = APIClient()
    client.authenticate()
    return client


@pytest.fixture(scope="session")  # Run after all tests finish
def generate_report(request):
    yield
    # Get the current date and time
    now = datetime.datetime.now()
    report_file = f"report_{now.strftime('%Y%m%d_%H%M%S')}.html"

    # Generate the HTML report
    pytest.main(['--html=' + report_file])


@pytest.fixture(scope='function')
def booking() -> Booking:
    return Booking()


@pytest.fixture(scope='function')
def create_booking() -> Booking:
    user_booking = Booking()
    yield user_booking.create_booking_id()
    user_booking.delete_booking_id()
