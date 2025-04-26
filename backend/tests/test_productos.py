import pytest
from fastapi.testclient import TestClient
from app.main import app

client: TestClient = TestClient(app)

def test_listar_top3():
    response = client.get("/productos/top3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_descargar_pdf_top3():
    response = client.get("/productos/top3/pdf")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
