from utils.booking import Booking


def test_create_valid_booking(api_client, booking: Booking):
    payload = booking.booking_data()
    response = api_client.post('/booking', json=payload)
    assert response.status_code == 200
    assert response.json()['booking'] == payload
    assert 'bookingid' in response.json()


def test_create_invalid_booking(api_client, booking: Booking):
    payload = booking.invalid_booking_data()
    response = api_client.post('/booking', json=payload)
    assert response.status_code == 500
    assert response.text == 'Internal Server Error'
