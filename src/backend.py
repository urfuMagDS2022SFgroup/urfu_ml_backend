from fastapi import FastAPI, Response, status

from src.api.models.basic import Info, Root
from src.api.models.errors import PredictionError, TimeOutError
from src.api.models.predicted import Predicted
from src.api.models.to_predict import ToPredict
from src.custom_exceptions import UnsupportedLanguageException, TimeOutException
from src.ml_models.predict_sentiments import PredictSentiment

__version__ = "0.6.1"

app = FastAPI(version=__version__)


@app.get("/", response_model=Root)
async def root(root_: Root = Root()) -> Root:
    """get info about group"""
    return root_


@app.get("/info")
async def get_info(info: Info = Info()) -> Info:
    """get info about task"""
    return info


@app.post("/predict", status_code=status.HTTP_200_OK)
async def create_prediction_ru(
        item: ToPredict, response: Response
) -> PredictionError | TimeOutError | Predicted:
    """Try to predict Russian text sentiment"""
    ps = PredictSentiment()
    try:
        ps.predict_sentiment_classifier(item.sentence)
        result = Predicted(
            lang=ps.predicted_language,
            score=ps.predicted_sentiment_score,
            sentiment=ps.predicted_sentiment_label,
        )
    except UnsupportedLanguageException:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return PredictionError(error=ps.error, lang=ps.predicted_language)
    except TimeOutException:
        response.status_code = status.HTTP_504_GATEWAY_TIMEOUT
        return TimeOutError(error="Something went wrong, please try again")
    return result
