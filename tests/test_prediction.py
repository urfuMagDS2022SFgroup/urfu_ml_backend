import pytest
from hamcrest import assert_that, equal_to, has_entries


class TestPrediction:
    @pytest.mark.parametrize("predict", ["Все будет хорошо!"], indirect=True)
    def test_create_prediction_ru(self, predict):
        assert_that(predict.status_code, equal_to(200), f"status code was {predict.status_code}")
        resp_json = predict.json()
        del resp_json["score"]
        assert_that(resp_json, has_entries({"lang": "ru", "sentiment": "NEUTRAL"}))

    @pytest.mark.parametrize("predict", ["Everything will be fine!"], indirect=True)
    def test_create_prediction_en(self, predict):
        assert_that(predict.status_code, equal_to(200), f"status code was {predict.status_code}")
        resp_json = predict.json()
        del resp_json["score"]
        assert_that(resp_json, has_entries({"lang": "en", "sentiment": "NEUTRAL"}))

    @pytest.mark.parametrize("predict", ["Buenas tardes Raimondo"], indirect=True)
    def test_create_prediction_error(self, predict):
        assert_that(predict.status_code, equal_to(400), f"status code was {predict.status_code}")
        resp_json = predict.json()
        assert_that(resp_json, has_entries({"error": "Expected Russian or English language but got es", "lang": "es"}))
