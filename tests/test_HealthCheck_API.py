
def test_get_HealthCheck(api_client):
    response = api_client.get("/ping")
    assert response.status_code == 201
