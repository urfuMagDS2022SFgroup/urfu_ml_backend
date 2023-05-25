FROM python:3.10-buster
ENV HOST="0.0.0.0"
ENV PORT="8000"
ENV POETRY_VERSION="1.4.2"
WORKDIR /back

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml /back/pyproject.toml
COPY poetry.toml /back/poetry.toml
COPY poetry.lock /back/poetry.lock
RUN poetry install --with torch

COPY src /back/src

ENV PYTHONPATH=/back
CMD poetry run uvicorn src.main:app --host $HOST --port $PORT
