# CHANGELOG — Evolución de la propuesta MLOps

## Versión inicial — Taller 1

La propuesta inicial contemplaba un pipeline básico para una solución médica simulada: recepción de datos, validación básica, función predictiva simulada, API Flask, Docker y ejecución local.

## Evolución intermedia — Taller 2

La solución se llevó a GitHub, incorporando ramas, Pull Requests, nuevos requerimientos, pruebas unitarias, GitHub Actions, construcción de imagen Docker y publicación en GitHub Packages.

## Versión actual — Taller 3

La propuesta actual reestructura el pipeline hacia una arquitectura MLOps cloud-first con Azure Machine Learning, MLflow, Model Registry, FastAPI, monitoreo, detección de drift y reentrenamiento controlado.

| Elemento | Propuesta inicial | Propuesta actual | Cambio realizado | Justificación |
|---|---|---|---|---|
| Alcance | Pipeline local y académico | Pipeline MLOps cloud-first | Se amplía hacia operación gestionada en nube | Representa un ciclo de vida realista |
| Modelo | Función simulada | Modelo entrenable, evaluable y versionado | Se propone evolución hacia ML real | Permite entrenamiento y mejora |
| Datos | Entrada manual JSON | Datos en Azure Blob Storage | Se centraliza almacenamiento | Mejora trazabilidad |
| API | Flask | FastAPI | Migración propuesta | Mejora validación y documentación |
| Docker | Imagen local | Imagen integrada al CI/CD | Se conecta a despliegue cloud | Mejora portabilidad |
| CI/CD | No incluido | GitHub Actions | Automatización de pruebas y build | Reduce errores manuales |
| Experimentos | Sin tracking | MLflow Tracking | Registro de métricas y artefactos | Permite comparar modelos |
| Registro | No existía | Azure ML Model Registry | Versionamiento y promoción | Control de producción |
| Despliegue | Local | Azure ML Managed Online Endpoint | URL estable de inferencia | Operación cloud |
| Monitoreo | Básico | Azure Monitor + Evidently AI | Logs, métricas y drift | Detecta degradación |
| Reentrenamiento | Conceptual | Controlado por métricas y drift | Ciclo de mejora continua | Mantiene desempeño |
