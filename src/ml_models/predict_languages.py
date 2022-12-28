from typing import Any

import torch
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class CheckText(BaseModel):
    text: str


class PredictLanguage:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
        self.model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")

    def predict_language(self, to_recognize: str) -> Any:
        inputs = self.tokenizer(to_recognize, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        return self.model.config.id2label[predicted_class_id]
