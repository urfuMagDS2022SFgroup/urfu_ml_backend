from transformers import pipeline


def classifier(text: str):
    cls = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
    return cls(text)


if __name__ == "__main__":
    print("Please enter your phrase in Russian: ")
    sentence = input()
    predicted_sentiment = classifier(sentence)
    print(
        f"With probability {round(predicted_sentiment[0]['score'], 3)} sentiment was {predicted_sentiment[0]['label']}")
