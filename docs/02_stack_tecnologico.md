# Stack tecnológico propuesto

| Capa | Tecnología | Rol | Justificación |
|---|---|---|---|
| Código fuente | GitHub | Versionamiento y PRs | Mantiene trazabilidad y continuidad con Taller 2 |
| CI/CD | GitHub Actions | Pruebas, build y publicación | Automatiza validación y entrega |
| Lenguaje | Python | Entrenamiento, API y scripts | Estándar para ML |
| API | FastAPI | Inferencia | Evoluciona Flask hacia robustez y documentación |
| Contenedores | Docker | Empaquetado | Reproducibilidad |
| Registro | GHCR / Azure Container Registry | Publicación de imágenes | Soporte a despliegue cloud |
| Datos | Azure Blob Storage | Almacenamiento | Centralización y trazabilidad |
| Entrenamiento | Azure ML Jobs | Entrenamiento gestionado | Evita dependencia local |
| Experimentos | MLflow Tracking | Parámetros, métricas y artefactos | Comparación de modelos |
| Modelos | Azure ML Model Registry | Versionamiento y promoción | Gobierno de modelos |
| Despliegue | Azure ML Managed Online Endpoint | Inferencia en tiempo real | URL estable para consumo |
| Monitoreo | Azure Monitor / Application Insights | Observabilidad | Latencia, errores y disponibilidad |
| Drift | Evidently AI / Azure ML Monitoring | Detección de cambios | Soporte a reentrenamiento |
| Documentación | Markdown + Mermaid | Entregable académico | Versionable y claro |
