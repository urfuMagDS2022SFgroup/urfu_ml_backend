import json

from fastapi import FastAPI, Response, status

from src.api.models.basic import Info, Root
from src.api.models.errors import PredictionError
from src.api.models.predicted import Predicted
from src.api.models.to_predict import ToPredict
from src.ml_models.predict_sentiments import PredictSentiment, WrongLanguage

__version__ = "0.3.1"

app = FastAPI(version=__version__)


@app.get("/", response_model=Root)
async def root(root_: Root = Root()) -> Root:
    """get info about group"""
    return root_


@app.get("/info")
async def get_info(info: Info = Info()) -> Info:
    """get info about task"""
    return info


@app.post("/predict/ru", status_code=status.HTTP_200_OK)
async def create_prediction_ru(item: ToPredict, response: Response) -> Predicted | PredictionError:
    """Try to predict Russian sentence or text sentiment"""
    sentiment_predict = PredictSentiment()
    try:
        sentiment_predict.predict_sentiment_classifier(item.sentence)
        result = Predicted(
            lang=sentiment_predict.predicted_language,
            score=sentiment_predict.predicted_sentiment_score,
            sentiment=sentiment_predict.predicted_sentiment_label
        )
    except WrongLanguage:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return PredictionError(error=sentiment_predict.error, lang=sentiment_predict.predicted_language)
    return result


@app.post("/predict/en")
async def create_prediction_en(item: ToPredict):
    """Try to predict English sentence or text sentiment"""
    sentiment_predict = PredictSentiment()
    sentiment_predict.predict_sentiment_classifier(item.sentence)
    result = sentiment_predict.__dict__
    return json.dumps(result)
