from transformers import pipeline


def classifier(text: str):
    cls = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
    return cls(text)


print(classifier("Я обожаю инженерию машинного обучения!"))
