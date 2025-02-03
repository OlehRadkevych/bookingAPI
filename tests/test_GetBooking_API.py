from schema import Schema, Use, Or


def test_get_booking_valid(api_client, create_booking):
    booking_id = create_booking
    response = api_client.get(f'/booking/{booking_id}')

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

    assert response.status_code == 200
    assert schema.is_valid(response.json())


def test_get_booking_without_param(api_client, booking):
    booking_id = None
    response = api_client.get(f'/booking/{booking_id}')
    assert response.status_code == 404
    assert response.text == 'Not Found'
