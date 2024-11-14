import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_results():
    response = client.get("/api/results")
    assert response.status_code == 200
    assert "results" in response.json()

def test_get_powerbi_schema():
    response = client.get("/api/powerbi/schema")
    assert response.status_code == 200
    assert "tables" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"} 