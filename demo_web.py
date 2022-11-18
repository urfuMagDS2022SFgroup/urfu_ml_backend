import streamlit as st
#import sample_model as sample_model
from transformers import pipeline

class sample_model:
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

#@st.cache(allow_output_mutation=True)

def load_sentence():
    text_input = st.text_input('')
    if text_input!='':
        st.write('your phrase:', text_input)
        return text_input
    else:
        return None


st.title("Practice 2 - Create web page using streamlit")
message = "## Please enter your phrase in Russian:"
st.markdown(message)

sentence = load_sentence()
if sentence != None:
    a=sample_model(sentence)
    report=f"With probability {a.predicted_sentiment_label} sentiment was {a.predicted_sentiment_score}"
    st.markdown(report)