# Propuesta general del pipeline MLOps reestructurado

## 1. Introducción

La propuesta reestructura el pipeline MLOps inicial desarrollado para una solución médica simulada. La versión inicial permitía recibir datos básicos de un paciente, validar entradas, ejecutar una función predictiva simulada, exponer la predicción mediante API Flask y empaquetar la aplicación con Docker.

La propuesta actual amplía ese flujo hacia un pipeline MLOps integral, trazable, automatizable y preparado para nube, usando Azure Machine Learning como plataforma principal.

## 2. Contexto

El caso de estudio corresponde a una solución médica simulada que clasifica el estado de un paciente a partir de variables como edad, presión arterial y nivel de síntomas.

Aunque los talleres anteriores usaron una función basada en reglas, el pipeline actual considera la evolución hacia un modelo real, entrenado con datos históricos, evaluado con métricas y gobernado mediante un registro de modelos.

## 3. Objetivo

Diseñar un pipeline MLOps que cubra gestión de datos, entrenamiento, tracking, evaluación, registro, aprobación, empaquetado, CI/CD, despliegue, inferencia, monitoreo, detección de drift y reentrenamiento.

## 4. Supuestos

- Los datos clínicos serán anonimizados.
- La solución no reemplaza el criterio médico.
- Azure será la nube principal.
- GitHub será la fuente principal de código.
- GitHub Actions automatizará pruebas, build y despliegue.
- MLflow registrará experimentos, métricas, parámetros y artefactos.
- Azure ML Model Registry controlará versiones de modelos.
- FastAPI será la API productiva propuesta.
- El reentrenamiento requiere validación técnica y funcional.

## 5. Etapas del pipeline

1. Definición del problema médico.
2. Fuentes de datos clínicos.
3. Ingesta de datos.
4. Almacenamiento en Azure Blob Storage.
5. Validación y calidad de datos.
6. Preparación de datos.
7. Entrenamiento en Azure ML Training Jobs.
8. Tracking de experimentos con MLflow.
9. Evaluación de métricas.
10. Registro en Azure ML Model Registry.
11. Aprobación y promoción del modelo.
12. Empaquetado con FastAPI y Docker.
13. CI/CD con GitHub Actions.
14. Publicación en registro de contenedores.
15. Despliegue en Azure ML Managed Online Endpoint.
16. Inferencia mediante API.
17. Registro de logs y predicciones.
18. Monitoreo con Azure Monitor y Application Insights.
19. Detección de drift con Evidently AI o Azure ML Monitoring.
20. Reentrenamiento controlado.

## 6. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Uso clínico indebido | Aclarar que es solución académica y requiere validación médica |
| Datos sesgados | Validación, análisis de distribución y revisión experta |
| Drift | Monitoreo con Evidently AI o Azure ML Monitoring |
| Modelo no validado | Uso de Model Registry y aprobación previa |
| Fallas operativas | Azure Monitor, logs y alertas |
| Costos cloud | Cómputo bajo demanda y eliminación de recursos no usados |

## 7. Conclusión

La propuesta convierte el pipeline inicial en una arquitectura MLOps integral con nube, automatización, tracking, registro de modelos, gobierno, monitoreo y reentrenamiento.
