import json
from pathlib import Path
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("data/processed/pacientes_sinteticos.csv")
OUTPUT_DIR = Path("outputs/model")
MODEL_PATH = OUTPUT_DIR / "model.pkl"
METADATA_PATH = OUTPUT_DIR / "metadata.json"

def cargar_datos(data_path: Path = DATA_PATH) -> pd.DataFrame:
    if not data_path.exists():
        raise FileNotFoundError("No existe el dataset. Ejecute: python -m src.data.generate_dataset")
    df = pd.read_csv(data_path)
    required = {"edad", "presion", "sintomas", "diagnostico"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")
    return df

def entrenar_modelo(data_path: Path = DATA_PATH):
    df = cargar_datos(data_path)
    X = df[["edad", "presion", "sintomas"]]
    y = df["diagnostico"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    params = {"n_estimators": 120, "max_depth": 8, "random_state": 42, "class_weight": "balanced"}
    mlflow.set_experiment("clasificacion-medica-simulada")
    with mlflow.start_run(run_name="random-forest-medico-simulado"):
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision_macro": precision_score(y_test, y_pred, average="macro", zero_division=0),
            "recall_macro": recall_score(y_test, y_pred, average="macro", zero_division=0),
            "f1_macro": f1_score(y_test, y_pred, average="macro", zero_division=0),
        }
        for k, v in params.items():
            mlflow.log_param(k, v)
        for k, v in metrics.items():
            mlflow.log_metric(k, float(v))
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        metadata = {"model_type": "RandomForestClassifier", "features": ["edad", "presion", "sintomas"], "target": "diagnostico", "metrics": metrics, "params": params}
        METADATA_PATH.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
        mlflow.log_artifact(str(MODEL_PATH))
        mlflow.log_artifact(str(METADATA_PATH))
        mlflow.sklearn.log_model(model, artifact_path="model")
        print(json.dumps(metrics, indent=2))
        return model, metrics

if __name__ == "__main__":
    entrenar_modelo()
