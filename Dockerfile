FROM python:3.10-buster

ADD . /src
WORKDIR /src

#RUN pip install --no-cache-dir --upgrade -r ./requirments.txt
RUN pip install poetry

RUN poetry install --with torch,backend

CMD ["poetry", "run", "uvicorn", "src.backend:app", "--host", "0.0.0.0", "--port", "80"]
