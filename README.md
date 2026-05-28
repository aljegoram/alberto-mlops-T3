# Taller 3 — Pipeline MLOps reestructurado con Azure Machine Learning

Este paquete contiene la propuesta y los artefactos técnicos de soporte para el Taller 3.

## Contenido

```text
src/                         Código de datos, entrenamiento e inferencia
azureml/                     Definiciones YAML para Azure Machine Learning
scripts/                     Scripts PowerShell para ejecución en Azure
tests/                       Pruebas unitarias
docs/                        Propuesta, stack, guía, diagrama y evidencias
.github/workflows/           Workflow de GitHub Actions
Dockerfile                   Imagen de la API FastAPI
requirements.txt             Dependencias Python
CHANGELOG.md                 Cambios frente a la propuesta inicial
```

## Ejecución local

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m src.data.generate_dataset
python -m src.training.train
python -m uvicorn src.inference.app.main:app --host 0.0.0.0 --port 8000
```

## Prueba de API

```bash
curl -X POST http://localhost:8000/predecir -H "Content-Type: application/json" -d "{\"edad\":85,\"presion\":190,\"sintomas\":10}"
```

## Pruebas

```bash
python -m pytest -q
```

## Nota académica

La solución médica es simulada y no debe usarse para diagnóstico real.
