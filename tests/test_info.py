import json

from hamcrest import assert_that, equal_to, has_entries


class TestInfo:
    def test_read_info(self, client):
        response = client.get("/info")
        response_object = json.loads(response.text)
        assert_that(response.status_code, equal_to(200), f"status code was {response.status_code}")
        expected = {"root": "/", "get_info": "/info", "create_prediction_ru": "/predict", "docs": "/docs"}
        assert_that(response_object, has_entries(expected))
