from typing import Optional

import streamlit as st

from models.predict_sentiment import PredictSentiment, WrongLanguage


def load_sentence() -> Optional[str]:
    text_input = st.text_input('')
    if text_input:
        return text_input
    return None


st.title("Practice 2 - Create a web page using streamlit")
st.markdown(body="## Please enter your phrase in Russian:")
sentence = load_sentence()


def predict_user_sentiment(txt: str) -> None:
    sentiment_predict = PredictSentiment()
    try:
        sentiment_predict.predict_sentiment_classifier(txt)
        report = f"With probability {sentiment_predict.predicted_sentiment_score} " \
                 f"sentiment was {sentiment_predict.predicted_sentiment_label}"
        if sentiment_predict.predicted_sentiment_label == "NEGATIVE":
            st.error(report, icon="💩")
        elif sentiment_predict.predicted_sentiment_label == "NEUTRAL":
            st.warning(report, icon="🤔")
        else:
            st.success(report, icon="😇")
    except WrongLanguage:
        st.error(sentiment_predict.error)
    finally:
        st.info("You can try another sentence", icon="ℹ️")


def run_the_app():
    if sentence:
        with st.spinner("JWST..."):
            predict_user_sentiment(sentence)


run_the_app()
