import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_sentiment_positive():
    text = "This is a wonderful day!"
    response = client.post("/sentiment_analysis", params={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "positive"}

def test_analyze_sentiment_negative():
    text = "I am feeling very sad."
    response = client.post("/sentiment_analysis", params={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "negative"}

def test_analyze_sentiment_neutral():
    text = "The sun is red in color"
    response = client.post("/sentiment_analysis", params={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "neutral"}
