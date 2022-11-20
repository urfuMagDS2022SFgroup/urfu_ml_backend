from transformers import pipeline


class SampleModel:
    input_text: str
    predicted_sentiment_score: int
    predicted_sentiment_label: str

    def __init__(self, sentence):
        self.input_text = sentence
        self.get_classifier()

    def get_classifier(self):
        cls = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
        predicted_sentiment = cls(self.input_text)
        self.predicted_sentiment_score = round(predicted_sentiment[0]['score'], 3)
        self.predicted_sentiment_label = predicted_sentiment[0]['label']
