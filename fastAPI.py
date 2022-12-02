from fastapi import FastAPI
from pydantic import BaseModel
from nlp_model import NLPModel
import json
from io import StringIO
io = StringIO()

class Prediction(BaseModel):
    sentence: str
    
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/info/")
async def get_info():
    return {"info": "Practice 3 - fastAPI"}

@app.post("/predict/ru/")
async def create_prediction(item: Prediction):
    sentiment_predict = NLPModel(item.sentence)
    result=sentiment_predict.__dict__
    return json.dumps(result)

@app.post("/predict/")
async def create_prediction(item: Prediction):
    sentiment_predict = NLPModel(item.sentence)
    sentiment_predict.get_sentiment_en_classifier()
    result=sentiment_predict.__dict__
    return json.dumps(result)