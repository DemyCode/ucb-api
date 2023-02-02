import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_client():
    yield TestClient(app)


def test_ping(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
