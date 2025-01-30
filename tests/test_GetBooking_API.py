from schema import Schema, Use, Or


def test_get_booking_valid(api_client, booking):
    booking_id = booking.create_booking_valid_data()
    response = api_client.get(f'/booking/{booking_id}')
    assert response.status_code == 200

    schema = Schema({
        'firstname': str,
        'lastname': str,
        'totalprice': Or(int, float),
        'depositpaid': bool,
        'bookingdates': {
            'checkin': Use(str),
            'checkout': Use(str)
        },
        'additionalneeds': Or(str, None)
    })
    assert schema.is_valid(response.json())


def test_get_booking_without_param(api_client, booking):
    booking_id = None
    response = api_client.get(f'/booking/{booking_id}')
    assert response.status_code == 404
    assert response.text == 'Not Found'
