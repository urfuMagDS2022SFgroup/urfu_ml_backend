from pydantic import BaseModel


class ToPredict(BaseModel):
    sentence: str
