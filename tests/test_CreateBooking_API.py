from utils.user_booking import User_booking
def test_CreateValidBooking(api_client):
    user_booking = User_booking()
    payload = user_booking.valid_data()
    response = api_client.post('/booking',json=payload)
    assert response.status_code == 200
    assert response.json()['booking'] == payload
    assert 'bookingid' in response.json()

def test_CreateInvalidBooking(api_client):
    user_booking = User_booking()
    payload = user_booking.invalid_data()
    response = api_client.post('/booking',json=payload)
    assert response.status_code == 500
    assert response.text == 'Internal Server Error'


