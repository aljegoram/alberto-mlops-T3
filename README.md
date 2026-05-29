# Taller 3 — Pipeline MLOps reestructurado con Azure Machine Learning

## 1. Información general

**Repositorio:** `alberto-mlops-T3`
**Caso de estudio:** solución médica simulada para clasificación del estado de un paciente.
**Objetivo del taller:** proponer y soportar un pipeline MLOps completo, claro y viable, incorporando etapas, tecnologías, supuestos, diagrama general y registro de cambios frente a la propuesta inicial.

Este repositorio presenta la evolución de una solución local basada en una función simulada hacia una propuesta MLOps cloud-first soportada con Azure Machine Learning, MLflow, Docker, FastAPI, GitHub Actions y Azure ML Model Registry.

---

## 2. Contexto del problema

El caso de estudio corresponde a una solución médica simulada que recibe variables básicas de un paciente, como:

* edad;
* presión arterial;
* nivel de síntomas.

A partir de esas variables, la solución clasifica el estado del paciente en categorías como:

* `NO ENFERMO`;
* `ENFERMEDAD LEVE`;
* `ENFERMEDAD AGUDA`;
* `ENFERMEDAD CRÓNICA`;
* `ENFERMEDAD TERMINAL`.


---

## 3. Objetivo del pipeline MLOps

El objetivo del pipeline propuesto es cubrir el ciclo de vida completo de una solución de machine learning:

1. definición del problema;
2. ingesta y almacenamiento de datos;
3. validación y preparación de datos;
4. entrenamiento del modelo;
5. tracking de experimentos con MLflow;
6. evaluación mediante métricas;
7. registro y versionamiento del modelo;
8. aprobación y promoción del modelo;
9. empaquetado con Docker;
10. exposición mediante API de inferencia;
11. automatización CI/CD;
12. despliegue en entorno cloud;
13. monitoreo;
14. detección de drift;
15. reentrenamiento controlado.

---

## 4. Diagrama general del pipeline

El diagrama principal del pipeline MLOps se encuentra en:

* [`docs/diagrama_pipeline_mlops.svg`](docs/diagrama_pipeline_mlops.svg)
* [`docs/diagrama_pipeline_mlops.mmd`](docs/diagrama_pipeline_mlops.mmd)

El flujo general propuesto es:

```text
Definición del problema médico
→ Fuentes de datos clínicos
→ Ingesta de datos
→ Azure Blob Storage
→ Validación y calidad de datos
→ Preparación de datos
→ Azure ML Training Jobs
→ MLflow Tracking
→ Evaluación de métricas
→ Azure ML Model Registry
→ Aprobación y promoción
→ FastAPI + Docker
→ GitHub Actions CI/CD
→ Container Registry
→ Azure ML Managed Online Endpoint
→ API de inferencia
→ Logs y predicciones
→ Azure Monitor / Application Insights
→ Evidently AI / Drift Monitoring
→ Reentrenamiento controlado
```

---

## 5. Propuesta general del pipeline

La propuesta completa está documentada en:

[`docs/01_propuesta_pipeline_mlops.md`](docs/01_propuesta_pipeline_mlops.md)

### 5.1 Etapas principales

| Etapa                   | Descripción                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| Definición del problema | Se define el objetivo de clasificación médica simulada y las métricas relevantes.    |
| Gestión de datos        | Se generan o reciben datos, se almacenan y se preparan para entrenamiento.           |
| Validación de datos     | Se revisan rangos, completitud y consistencia antes de entrenar o predecir.          |
| Entrenamiento           | Se entrena un modelo `RandomForestClassifier` sobre datos sintéticos.                |
| Tracking                | Se registran parámetros, métricas y artefactos usando MLflow.                        |
| Evaluación              | Se calculan métricas como accuracy, precision, recall y F1-score.                    |
| Registro del modelo     | Se registra el modelo en Azure ML Model Registry.                                    |
| Inferencia              | Se expone la predicción mediante una API FastAPI.                                    |
| CI/CD                   | GitHub Actions ejecuta pruebas, entrenamiento local y construcción Docker.           |
| Monitoreo               | Se propone monitorear latencia, errores, predicciones, drift y desempeño.            |
| Reentrenamiento         | Se propone reentrenar cuando haya drift, caída de métricas o nuevos datos validados. |

---

## 6. Tecnologías propuestas

La justificación completa del stack tecnológico está en:

[`docs/02_stack_tecnologico.md`](docs/02_stack_tecnologico.md)

| Componente     | Tecnología propuesta                 | Justificación                                                                  |
| -------------- | ------------------------------------ | ------------------------------------------------------------------------------ |
| Repositorio    | GitHub                               | Versionamiento, ramas, commits y trazabilidad.                                 |
| Automatización | GitHub Actions                       | CI/CD para pruebas, entrenamiento local, build Docker y publicación de imagen. |
| Lenguaje       | Python                               | Lenguaje base para entrenamiento, inferencia y automatización ML.              |
| API            | FastAPI                              | API moderna, validación automática y documentación interactiva.                |
| Empaquetado    | Docker                               | Reproducibilidad y portabilidad de la solución.                                |
| Tracking       | MLflow                               | Registro de experimentos, métricas, parámetros y artefactos.                   |
| Cloud ML       | Azure Machine Learning               | Entrenamiento gestionado, tracking, modelos y endpoints.                       |
| Model Registry | Azure ML Model Registry              | Versionamiento y gobierno del modelo.                                          |
| Monitoreo      | Azure Monitor / Application Insights | Observabilidad operativa del servicio.                                         |
| Drift          | Evidently AI / Azure ML Monitoring   | Detección de cambios en datos y comportamiento del modelo.                     |
| Documentación  | Markdown + Mermaid                   | Documentación versionable y clara para la entrega.                             |

---

## 7. Supuestos principales

* Los datos usados son sintéticos.

## 8. Implementación de soporte incluida en el repositorio

El repositorio contiene la propuesta documental y artefactos técnicos de soporte:

```text
src/
├── data/
│   └── generate_dataset.py
├── training/
│   └── train.py
└── inference/
    ├── app/
    │   ├── main.py
    │   ├── predictor.py
    │   └── schemas.py
    └── score.py
```

### 8.1 Generación de datos sintéticos

```bash
python -m src.data.generate_dataset
```

### 8.2 Entrenamiento local con MLflow

```bash
python -m src.training.train
```

### 8.3 Ejecución de pruebas

```bash
python -m pytest -q
```

### 8.4 Ejecución de API FastAPI

```bash
python -m uvicorn src.inference.app.main:app --host 0.0.0.0 --port 8000
```

### 8.5 Prueba de endpoint

```bash
curl -X POST http://localhost:8000/predecir -H "Content-Type: application/json" -d "{\"edad\":85,\"presion\":190,\"sintomas\":10}"
```

Respuesta esperada:

```json
{
  "resultado": "ENFERMEDAD TERMINAL",
  "fuente_modelo": "modelo_entrenado",
  "version_modelo": "v3.0-propuesta"
}
```

---

## 9. Automatización CI/CD

El workflow de GitHub Actions está en:

[`/.github/workflows/taller3-azure-mlops.yml`](.github/workflows/taller3-azure-mlops.yml)

El pipeline automatizado ejecuta:

1. descarga del código;
2. configuración de Python;
3. instalación de dependencias;
4. pruebas unitarias;
5. generación de dataset;
6. entrenamiento del modelo;
7. construcción de imagen Docker;
8. publicación de imagen en GitHub Container Registry.

---

## 10. Azure Machine Learning

El repositorio incluye artefactos para ejecutar entrenamiento en Azure ML:

```text
azureml/
├── environment.yml
├── train-job.yml
├── endpoint.yml
└── deployment.yml
```

Durante el desarrollo del taller se validó el flujo en Azure Machine Learning con:

* workspace `aml-mlops-taller3`;
* compute cluster `cpu-cluster`;
* training job ejecutado correctamente;
* experimento `clasificacion-medica-simulada`;
* métricas registradas con MLflow;
* modelo registrado como `modelo-medico-simulado`, versión `1`.

El job de Azure ML ejecuta:

```bash
python -m pip install --upgrade pip &&
python -m pip install -r requirements.txt &&
python -m src.data.generate_dataset &&
python -m src.training.train
```

---

## 11. Métricas registradas

El entrenamiento registra las siguientes métricas:

| Métrica         | Descripción                                              |
| --------------- | -------------------------------------------------------- |
| accuracy        | Porcentaje general de predicciones correctas.            |
| precision_macro | Precisión promedio entre clases.                         |
| recall_macro    | Capacidad promedio de detectar correctamente cada clase. |
| f1_macro        | Balance entre precision y recall.                        |


---

## 12. CHANGELOG

El registro de cambios entre la propuesta inicial y la propuesta actual está en:

[`CHANGELOG.md`](CHANGELOG.md)

El CHANGELOG muestra la evolución desde:

```text
Taller 1:
API Flask + función simulada + Docker local

Taller 2:
GitHub + ramas + PRs + pruebas + GitHub Actions + Docker Packages

Taller 3:
Azure ML + MLflow + Model Registry + FastAPI + Docker + monitoreo + drift + reentrenamiento
```

---

## 13. Estructura del repositorio

```text
alberto-mlops-T3/
├── README.md
├── CHANGELOG.md
├── Dockerfile
├── requirements.txt
├── azureml/
│   ├── environment.yml
│   ├── train-job.yml
│   ├── endpoint.yml
│   └── deployment.yml
├── docs/
│   ├── 01_propuesta_pipeline_mlops.md
│   ├── 02_stack_tecnologico.md
│   ├── 03_guia_ejecucion_azure.md
│   ├── 04_evidencias_requeridas.md
│   ├── diagrama_pipeline_mlops.mmd
│   └── diagrama_pipeline_mlops.svg
├── src/
│   ├── data/
│   ├── training/
│   └── inference/
├── tests/
├── scripts/
└── .github/
    └── workflows/
```

---

## 14. Relación con la rúbrica

| Criterio de calificación       | Evidencia en el repositorio                         |
| ------------------------------ | --------------------------------------------------- |
| Propuesta general del pipeline | `README.md` y `docs/01_propuesta_pipeline_mlops.md` |
| Diagrama principal             | `docs/diagrama_pipeline_mlops.svg`                  |
| Tecnologías propuestas         | `README.md` y `docs/02_stack_tecnologico.md`        |
| CHANGELOG                      | `CHANGELOG.md`                                      |

---

## 15. Conclusión

La propuesta final presenta un pipeline MLOps completo y viable, alineado con una solución médica simulada. El diseño cubre desde la gestión de datos y entrenamiento hasta CI/CD, registro del modelo, monitoreo, detección de drift y reentrenamiento controlado. Además, el repositorio incluye código funcional, pruebas, Docker, GitHub Actions y ejecución validada en Azure Machine Learning.
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
