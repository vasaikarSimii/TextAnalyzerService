import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_count_words():
    text = "New York University is good"
    response = client.post("/word_count", params={"text": text})
    assert response.status_code == 200
    assert response.json() == {"word_count": 5}
