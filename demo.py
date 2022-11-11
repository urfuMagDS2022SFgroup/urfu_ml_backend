from transformers import pipeline


def classifier(text: str):
    classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
    return classifier(text)


classifier("Я обожаю инженерию машинного обучения!")
