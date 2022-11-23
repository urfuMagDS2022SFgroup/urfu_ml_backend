from typing import Any

import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


class NLPModel:
    predicted_sentiment_score: int
    predicted_sentiment_label: str
    error: str

    def __init__(self, sentence: str) -> None:
        self.input_text = sentence
        self.predicted_language = self.predict_language()
        self.is_ru = True if self.predicted_language == "ru" else False
        self.get_sentiment_classifier()

    def get_sentiment_classifier(self):
        if self.is_ru:
            pipe = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
            predicted_sentiment = pipe(self.input_text)
            self.predicted_sentiment_score = round(predicted_sentiment[0]['score'], 3)
            self.predicted_sentiment_label = predicted_sentiment[0]['label']
        else:
            self.error = f"Ожидался русский язык а оказался {self.predicted_language}"

    def predict_language(self) -> Any:
        tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
        model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
        inputs = tokenizer(self.input_text, return_tensors="pt")

        with torch.no_grad():
            logits = model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        return model.config.id2label[predicted_class_id]
