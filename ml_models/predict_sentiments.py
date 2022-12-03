from transformers import pipeline

from ml_models.predict_languages import PredictLanguage


class WrongLanguage(Exception):
    """Exception raised if not Russian or English languages passed."""
    pass


class PredictSentiment:
    predicted_language: str
    predicted_sentiment_score: float | None
    predicted_sentiment_label: str
    error: str

    def __init__(self) -> None:
        self.predicted_language = ""
        self.predicted_sentiment_score = None
        self.predicted_sentiment_label = ""
        self.error = ""
        self.pl = PredictLanguage()
        self.pipe = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

    def predict_sentiment_classifier(self, input_text: str):
        if self._can_be_predicted(predicted_text=input_text):
            predicted_sentiment = self.pipe(input_text)
            self.predicted_sentiment_score = round(predicted_sentiment[0]['score'], 3)
            self.predicted_sentiment_label = predicted_sentiment[0]['label']
        else:
            self.error = f"Ожидался русский или английский язык а оказался {self.predicted_language}"
            raise WrongLanguage

    def _can_be_predicted(self, predicted_text) -> bool:
        self.predicted_language = self.pl.predict_language(to_recognize=predicted_text)
        return True if self.predicted_language in ["ru", "en"] else False


if __name__ == "__main__":
    text = "Кого за смертью посылать"
    text_es = "Buenas tardes Raimondo"
    ps = PredictSentiment()
    ps.predict_sentiment_classifier(input_text=text_es)
    print(ps.predicted_sentiment_label)
    print(ps.predicted_language)
    print(ps.error)
