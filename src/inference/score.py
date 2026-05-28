import json
from app.predictor import Predictor

predictor = Predictor()

def init():
    pass

def run(raw_data):
    data = json.loads(raw_data)
    return predictor.predict(int(data["edad"]), int(data["presion"]), int(data["sintomas"]))
