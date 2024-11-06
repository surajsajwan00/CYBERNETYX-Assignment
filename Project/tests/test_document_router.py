from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the RAG API"}

def test_upload_document():
    with open("sample.txt", "rb") as file:
        response = client.post("/upload", files={"file": ("sample.txt", file, "text/plain")})
    assert response.status_code == 200
    assert response.json()["status"] == "Document uploaded and ingested"

def test_query_document():
    response = client.get("/query", params={"query": "sample search text"})
    assert response.status_code == 200
    assert "results" in response.json()
