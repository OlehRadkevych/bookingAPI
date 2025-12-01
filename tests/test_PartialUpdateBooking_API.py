import pytest

from utils.booking import Booking
from tests.data.invalid_names import TEST_MATRIX
from tests.data.invalid_bookingdates import INVALID_BOOKINGDATES, INVALID_BOOKINGDATES_IDS


def test_partial_update_valid_booking(api_client, create_booking, booking: Booking):
    booking_id = create_booking
    payload ={
        "firstname": booking.firstname,
        "lastname": booking.lastname
    }

    response = api_client.patch(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 200
    assert payload["firstname"] in response.json().values()
    assert payload["lastname"] in response.json().values()


@pytest.mark.parametrize(
    "firstname, lastname, case_id",
    TEST_MATRIX,
    ids=[c[2] for c in TEST_MATRIX]
)
def test_partial_update_invalid_first_last_names(api_client, create_booking, booking: Booking, firstname, lastname, case_id):
    booking_id = create_booking
    payload ={
        "firstname": firstname,
        "lastname": lastname
    }

    response = api_client.patch(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["firstname"] not in response.json().values()
    assert payload["lastname"] not in response.json().values()


@pytest.mark.parametrize(
    "invalid_totalprice",[-1,0,None],ids=["negative_amount","zero","missing_totalprice"])
def test_partial_update_invalid_booking_negative_total_price(api_client, create_booking, booking: Booking, invalid_totalprice):
    booking_id = create_booking
    payload ={
        "totalprice": invalid_totalprice
    }

    response = api_client.patch(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["totalprice"] not in response.json().values()


@pytest.mark.parametrize(
    "invalid_bookingdates",INVALID_BOOKINGDATES,ids=INVALID_BOOKINGDATES_IDS)
def test_partial_update_invalid_booking_wrong_dates(api_client, create_booking, booking: Booking, invalid_bookingdates):
    booking_id = create_booking
    payload = {
        "bookingdates": invalid_bookingdates
    }

    response = api_client.patch(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert payload["bookingdates"] not in response.json().values()


def test_partial_update_invalid_booking(api_client, create_booking, booking: Booking):
    booking_id = create_booking
    payload = {
        "depositpaid": None
    }

    response = api_client.patch(f'/booking/{booking_id}', json=payload)

    assert response.status_code == 400
    assert response.text == 'Bad Request'
