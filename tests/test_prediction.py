import pytest


class TestPrediction:
    @pytest.mark.parametrize("predict", ["Все будет хорошо!"], indirect=True)
    def test_create_prediction_ru(self, predict):
        assert predict.status_code == 200
        resp_json = predict.json()
        del resp_json["score"]
        assert resp_json == {
            "lang": "ru",
            "sentiment": "NEUTRAL"
        }

    @pytest.mark.parametrize("predict", ["Everything will be fine!"], indirect=True)
    def test_create_prediction_en(self, predict):
        assert predict.status_code == 200
        resp_json = predict.json()
        del resp_json["score"]
        assert resp_json == {
            "lang": "en",
            "sentiment": "NEUTRAL"
        }

    @pytest.mark.parametrize("predict", ["Buenas tardes Raimondo"], indirect=True)
    def test_create_prediction_error(self, predict):
        assert predict.status_code == 400
        resp_json = predict.json()
        assert resp_json == {
            "error": "Expected Russian or English language but got es",
            "lang": "es"
        }
