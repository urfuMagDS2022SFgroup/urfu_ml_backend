from pydantic import BaseModel


class PredictionError(BaseModel):
    error: str
    lang: str


class TimeOutError(BaseModel):
    error: str


class CantFindModelError(BaseModel):
    error: str
