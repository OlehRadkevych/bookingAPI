import pytest
from utils.booking import Booking


@pytest.fixture(scope='function')
def booking() -> Booking:
    return Booking()


def test_get_booking_ids_all(api_client, booking: Booking):

    response = api_client.get("/booking")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_booking_ids_by_first_name(api_client, booking: Booking):
    params = {
        'firstname': booking.firstname
    }

    response = api_client.get("/booking", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_booking_ids_by_last_name(api_client, booking: Booking):
    params = {
        'lastname': booking.lastname
    }

    response = api_client.get("/booking", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_booking_ids_by_checkin_date(api_client, booking: Booking):
    params = {
        "checkin": booking.bookingdates['checkin']
    }

    response = api_client.get("/booking", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_booking_ids_by_checkout_date(api_client, booking: Booking):
    params = {
        "checkout": booking.bookingdates['checkout']
    }

    response = api_client.get("/booking", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
