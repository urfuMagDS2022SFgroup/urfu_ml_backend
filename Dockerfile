FROM python:3.10-buster
ENV HOST="0.0.0.0"
ENV PORT="8000"
ENV POETRY_VERSION="1.3.1"
WORKDIR /back

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml /back/pyproject.toml
COPY poetry.toml /back/poetry.toml
COPY poetry.lock /back/poetry.lock
RUN poetry install --with torch

COPY src /back/src

ENV PYTHONPATH=/back
CMD poetry run uvicorn src.backend:app --host $HOST --port $PORT
