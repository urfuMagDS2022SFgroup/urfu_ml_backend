from pydantic import BaseModel


class Info(BaseModel):
    root: str = "/"
    get_info: str = "/info"
    create_prediction_ru: str = "/predict/ru"
    create_prediction_en: str = "/predict/en"


class Root(BaseModel):
    message: str = "Welcome to UrFU ML Engineering 2022, Group 20 project"
    practice: str = "Practice 3 - Fast API"
    git_hub: str = "https://github.com/urfuMagDS2022SFgroup/sf_data_science_python"
    authors: list = [
        "Vladimir Katin <katin.v.v.@gmail.com>",
        "Anton Bessolitsyn <Anton.Bessolitsyn@hotmail.com>",
        "Anna Bezhenar <asbezhenar@gmail.com>",
        "Alexander Orlov <eaglophone@gmail.com>"
    ]
