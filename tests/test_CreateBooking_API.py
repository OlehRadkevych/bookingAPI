import pytest

from utils.booking import Booking
from tests.data.invalid_names import TEST_MATRIX
from tests.data.invalid_bookingdates import INVALID_BOOKINGDATES, INVALID_BOOKINGDATES_IDS


class TestCreateBooking:
    def test_create_valid_booking(self, api_client, create_booking, booking: Booking):
        payload = booking.booking_data()

        response = api_client.post('/booking', json=payload)

        assert response.status_code == 200
        assert response.json()['booking'] == payload
        assert 'bookingid' in response.json()


class TestCreatedBookingNegative:
    @pytest.mark.parametrize(
        "firstname, lastname, case_id",
        TEST_MATRIX,
        ids=[c[2] for c in TEST_MATRIX]
    )
    def test_create_invalid_first_last_names(self, api_client, booking: Booking, firstname, lastname, case_id):
        payload = booking.booking_data()
        payload["firstname"] = firstname
        payload["lastname"] = lastname

        response = api_client.post("/booking", json=payload)

        assert response.status_code == 400
        assert "bookingid" not in response.json()

    @pytest.mark.parametrize(
        "invalid_totalprice", [-1, 0, None], ids=["negative_amount", "zero", "missing_totalprice"])
    def test_create_invalid_booking_negative_total_price(self, api_client, booking: Booking, invalid_totalprice):
        payload = booking.booking_data()
        payload["totalprice"] = invalid_totalprice

        response = api_client.post("/booking", json=payload)

        assert response.status_code == 400
        assert "bookingid" not in response.json()

    @pytest.mark.parametrize(
        "invalid_bookingdates", INVALID_BOOKINGDATES, ids=INVALID_BOOKINGDATES_IDS)
    def test_create_invalid_booking_wrong_dates(self, api_client, booking: Booking, invalid_bookingdates):
        payload = booking.booking_data()
        payload["bookingdates"] = invalid_bookingdates

        response = api_client.post("/booking", json=payload)

        assert response.status_code == 400
        assert "bookingid" not in response.json()

    def test_create_invalid_booking(self, api_client, booking: Booking):
        payload = booking.invalid_booking_data()

        response = api_client.post('/booking', json=payload)

        assert response.status_code == 500
        assert response.text == 'Internal Server Error'
