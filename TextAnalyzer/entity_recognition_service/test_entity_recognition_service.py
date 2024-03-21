import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recognize_entities():
    text = "New York University is good in USA"
    response = client.post("/entity_recognition", params={"text": text})
    assert response.status_code == 200
    assert len(response.json()["entities"]) == 2  # Assuming 2 entities are recognized
