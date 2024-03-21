import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_service():
    #services = [ "word_count" ,  ]
    #ports = [ ]  
    service_name = "word_count"
    port = 8004
    response = client.post(f"/register?service_name={service_name}&port={port}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Voila! Service Registered Successfully {service_name}"}

def test_analyze_text():
    service_name = "word_count"
    port = 8002
    response = client.post(f"/register?service_name={service_name}&port={port}")
    text = "New York University is good"
    # Analyze text using the test service
    response = client.post("/textanalyzer", params={"service_name": service_name, "text": text})
    assert response.status_code == 200
    