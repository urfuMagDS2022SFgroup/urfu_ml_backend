import json
import logging

import streamlit as st
import requests

from frontend.constants import BACKEND_URL

logging.basicConfig(level=logging.DEBUG)

url = BACKEND_URL


def load_sentence() -> str | None:
    text_input = st.text_input(label="Text input")
    if text_input:
        return text_input
    return None


response_text = json.loads(requests.request(method="GET", url=url).text)
st.title(response_text["message"])

st.markdown(body=f"""### Authors:
- {response_text["authors"][0]}
- {response_text["authors"][1]}
- {response_text["authors"][2]}
- {response_text["authors"][3]}
""")
st.markdown(body="## Please enter your phrase in Russian or English and we will try to predict it's sentiment.")
sentence = load_sentence()

st.markdown(f"[our Git Hub]({response_text['git_hub']})")


def predict_user_sentiment(to_predict: dict) -> None:
    response = requests.request(method="POST", url=f"{url}predict", json=to_predict)
    resp_text = json.loads(response.text)
    resp_code = response.status_code
    if resp_code == 200:
        lang: str = resp_text["lang"]
        score: float = resp_text["score"]
        sentiment: str = resp_text["sentiment"]
        report = f"Your language predicted as {lang.upper()} and with probability {score} " \
                 f"the sentiment was {sentiment}"
        if sentiment == "NEGATIVE":
            st.error(report, icon="💩")
        elif sentiment == "NEUTRAL":
            st.warning(report, icon="🤔")
        else:
            st.success(report, icon="😇")
    elif resp_code == 400 or resp_code == 504:
        st.error(resp_text.error)
    else:
        st.error("Sorry, something went wrong")
    st.info("You can try another sentence", icon="ℹ️")


def app():
    if sentence:
        with st.spinner("JWST..."):
            predict_user_sentiment({"sentence": sentence})


app()
