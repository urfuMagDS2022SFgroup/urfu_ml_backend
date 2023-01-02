from typing import Any

from transformers import pipeline, Pipeline
import logging

from urllib3.exceptions import ConnectTimeoutError

from src.ml_models.predict_languages import PredictLanguage
from src.custom_exceptions import UnsupportedLanguageException, TimeOutException

logging.basicConfig(level=logging.DEBUG)


class PredictSentiment:
    predicted_language: str | None
    predicted_sentiment_score: float | None
    predicted_sentiment_label: str | None
    error: str | None

    def __init__(self) -> None:
        self.predicted_language: str | None
        self.predicted_sentiment_score: float | None
        self.predicted_sentiment_label: str | None
        self.error: str | None
        self.pl: Any = PredictLanguage()
        self.pipe: Pipeline = pipeline(task="sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")

    def predict_sentiment_classifier(self, input_text: str) -> None:
        if self._can_be_predicted(predicted_text=input_text):
            # Try to download model if not existed for 3 tries (15 sec)
            for i in range(3):
                try_ = i + 1
                try:
                    logging.debug(f"Try to implement prediction {try_} try")
                    predicted_sentiment = self.pipe(input_text)
                    self.predicted_sentiment_score = round(predicted_sentiment[0]['score'], 3)
                    self.predicted_sentiment_label = predicted_sentiment[0]['label']
                    return
                except ConnectTimeoutError:
                    logging.debug(f"Cannot download the model for {try_} try")
                    if i == 2:
                        self.error = f"Cannot complete prediction maybe huggingface.io cannot be reached"
                        raise TimeOutException
                    else:
                        continue
        else:
            self.error = f"Expected Russian or English language but got {self.predicted_language}"
            raise UnsupportedLanguageException

    def _can_be_predicted(self, predicted_text) -> bool:
        self.predicted_language = self.pl.predict_language(to_recognize=predicted_text)
        return True if self.predicted_language in ["ru", "en"] else False
