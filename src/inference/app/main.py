from fastapi import FastAPI
from src.inference.app.predictor import Predictor
from src.inference.app.schemas import PacienteInput, PrediccionOutput

app = FastAPI(title="Servicio Médico Simulado - Taller 3 MLOps", version="3.0.0")
predictor = Predictor()

@app.get("/health")
def health():
    return {"status": "ok", "service": "servicio-medico-simulado", "version": "3.0.0"}

@app.post("/predecir", response_model=PrediccionOutput)
def predecir(payload: PacienteInput):
    return predictor.predict(payload.edad, payload.presion, payload.sintomas)
