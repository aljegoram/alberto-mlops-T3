from fastapi.testclient import TestClient
from src.inference.app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predecir_enfermedad_terminal():
    response = client.post("/predecir", json={"edad": 85, "presion": 190, "sintomas": 10})
    assert response.status_code == 200
    assert response.json()["resultado"] == "ENFERMEDAD TERMINAL"

def test_validacion_sintomas_fuera_de_rango():
    response = client.post("/predecir", json={"edad": 85, "presion": 190, "sintomas": 20})
    assert response.status_code == 422
