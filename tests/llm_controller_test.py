from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_generate():
    response = client.post(
        "/api/v1/generate",
        json={"prompt": "Test unitario", "temperature": 0.8}
    )
    
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)