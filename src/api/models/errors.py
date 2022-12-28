from pydantic import BaseModel


class PredictionError(BaseModel):
    error: str
    lang: str
