from pydantic import BaseModel


class Predicted(BaseModel):
    lang: str
    score: float
    sentiment: str
