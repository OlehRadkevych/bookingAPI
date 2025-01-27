
def test_get_Booking_ids_All(api_client):
    response = api_client.get("/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_Booking_ids_by_first_name(api_client):
    data = {
        firstname = faker.
    }
    response = api_client.get("/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
