

class TestGetHealthCheck:
    def test_get_health_check(self, api_client):
    
        response = api_client.get("/ping")
    
        assert response.status_code == 201
