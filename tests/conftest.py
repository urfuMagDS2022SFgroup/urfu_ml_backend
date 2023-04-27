import pytest
from fastapi.testclient import TestClient

from src.api.models.to_predict import ToPredict
from src.main import app


@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="function")
def predict(request, client):
    payload = ToPredict(sentence=request.param).dict()
    return client.post(
        "/predict",
        json=payload,
    )
