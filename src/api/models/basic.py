from pydantic import BaseModel


class Info(BaseModel):
    root: str = "/"
    get_info: str = "/info"
    create_prediction_ru: str = "/predict"
    docs: str = "/docs"


class Root(BaseModel):
    message: str = "Welcome to UrFU ML Engineering 2022, Group 20 project"
    practice: str = "Practice 4 - Fast API with tests"
    git_hub_back: str = "https://github.com/urfuMagDS2022SFgroup/urfu_ml_backend"
    git_hub_front: str = "https://github.com/urfuMagDS2022SFgroup/streamlit_frontend"
    authors: list[str] = [
        "Vladimir Katin <katin.v.v.@gmail.com>",
        "Anton Bessolitsyn <Anton.Bessolitsyn@hotmail.com>",
        "Alexander Orlov <eaglophone@gmail.com>",
        "Anna Bezhenar <asbezhenar@gmail.com>",
    ]
