from fastapi import APIRouter, Response, status

from src.api.models.errors import PredictionError, TimeOutError
from src.api.models.predicted import Predicted
from src.api.models.to_predict import ToPredict
from src.custom_exceptions import TimeOutException, UnsupportedLanguageException
from src.ml_models.predict_sentiments import PredictSentiment

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def create_prediction_ru(item: ToPredict, response: Response) -> PredictionError | TimeOutError | Predicted:
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
