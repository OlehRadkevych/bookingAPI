import pytest

from utils.booking import Booking
from tests.data.invalid_names import TEST_MATRIX
from tests.data.invalid_bookingdates import INVALID_BOOKINGDATES, INVALID_BOOKINGDATES_IDS


def test_update_valid_booking(api_client, create_booking, booking: Booking):
    booking_id = create_booking
    payload = booking.booking_data()

    response = api_client.put(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 200
    assert response.json() == payload


@pytest.mark.parametrize(
    "firstname, lastname, case_id",
    TEST_MATRIX,
    ids=[c[2] for c in TEST_MATRIX]
)
def test_update_invalid_first_last_names(api_client, create_booking, booking: Booking, firstname, lastname, case_id):
    booking_id = create_booking
    payload = booking.booking_data()
    payload["firstname"] = firstname
    payload["lastname"] = lastname

    response = api_client.put(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["firstname"] not in response.json().values()
    assert payload["lastname"] not in response.json().values()


@pytest.mark.parametrize(
    "invalid_totalprice",[-1,0,None],ids=["negative_amount","zero","missing_totalprice"])
def test_update_invalid_booking_negative_total_price(api_client, create_booking, booking: Booking, invalid_totalprice):
    booking_id = create_booking
    payload = booking.booking_data()
    payload["totalprice"] = invalid_totalprice

    response = api_client.put(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["totalprice"] not in response.json().values()


@pytest.mark.parametrize(
    "invalid_bookingdates",INVALID_BOOKINGDATES,ids=INVALID_BOOKINGDATES_IDS)
def test_update_invalid_booking_wrong_dates(api_client, create_booking, booking: Booking, invalid_bookingdates):
    booking_id = create_booking
    payload = booking.booking_data()
    payload["bookingdates"] = invalid_bookingdates

    response = api_client.put(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["bookingdates"] not in response.json().values()


def test_update_invalid_booking(api_client, create_booking, booking: Booking):
    booking_id = create_booking
    payload = booking.invalid_booking_data()

    response = api_client.put(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert response.text == 'Bad Request'
