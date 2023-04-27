from fastapi import FastAPI

from src.api.handlers import info_handler, predict_handler, root_handler

app = FastAPI(version="0.7.0")

app.include_router(root_handler.router)
app.include_router(info_handler.router)
app.include_router(predict_handler.router)
