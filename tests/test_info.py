class TestInfo:
    def test_read_info(self, client):
        response = client.get("/info")
        assert response.status_code == 200
        expected = {
            "root": "/",
            "get_info": "/info",
            "create_prediction_ru": "/predict/ru"
        }
        assert response.json() == expected
