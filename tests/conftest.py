import os
from pathlib import Path

import pytest
from utils.api_client import APIClient
from utils.booking import Booking
import datetime


@pytest.fixture(scope="module")
def api_client():
    client = APIClient()
    client.authenticate()
    return client


# @pytest.fixture(scope="session")
# def generate_report(request):
#     yield
#     reports_dir = Path(request.config.rootpath) / "reports"
#     reports_dir.mkdir(exist_ok=True)
#     now = datetime.datetime.now()
#     report_file = reports_dir / f"report_{now.strftime('%Y%m%d_%H%M%S')}.html"
#     pytest.main([f"--html={report_file}"])


@pytest.fixture(scope='function')
def booking() -> Booking:
    return Booking()


@pytest.fixture(scope='function')
def create_booking() -> Booking:
    user_booking = Booking()
    yield user_booking.create_booking_id()
    user_booking.delete_booking_id()
