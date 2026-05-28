import os
from pathlib import Path
import joblib
import pandas as pd

DEFAULT_MODEL_PATH = Path("outputs/model/model.pkl")

def regla_simulada(edad: int, presion: int, sintomas: int) -> str:
    if edad >= 80 and sintomas >= 9 and presion >= 180:
        return "ENFERMEDAD TERMINAL"
    if edad >= 60 and sintomas >= 8 and presion >= 150:
        return "ENFERMEDAD CRÓNICA"
    if sintomas <= 1 and presion < 130:
        return "NO ENFERMO"
    if sintomas <= 4 and presion < 140:
        return "ENFERMEDAD LEVE"
    return "ENFERMEDAD AGUDA"

class Predictor:
    def __init__(self):
        self.model_path = Path(os.getenv("MODEL_PATH", str(DEFAULT_MODEL_PATH)))
        self.model = None
        self.fuente_modelo = "regla_simulada"
        if self.model_path.exists():
            self.model = joblib.load(self.model_path)
            self.fuente_modelo = "modelo_entrenado"

    def predict(self, edad: int, presion: int, sintomas: int) -> dict:
        if self.model is None:
            resultado = regla_simulada(edad, presion, sintomas)
        else:
            X = pd.DataFrame([{"edad": edad, "presion": presion, "sintomas": sintomas}])
            resultado = self.model.predict(X)[0]
        return {"resultado": resultado, "fuente_modelo": self.fuente_modelo, "version_modelo": "v3.0-propuesta"}
