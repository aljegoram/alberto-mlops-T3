# Guía de ejecución en Azure

## Prerrequisitos

- Cuenta de Azure activa.
- Azure CLI.
- Extensión Azure ML CLI v2.
- Permisos para crear Resource Group y Azure ML Workspace.

## Pasos

```powershell
az extension add -n ml -y
az login
.\scripts\02_crear_recursos_azure.ps1
.\scripts\03_ejecutar_entrenamiento_azure.ps1
```

Luego revisar en Azure ML Studio:

- Workspace.
- Compute cluster.
- Job de entrenamiento.
- Experimento MLflow.
- Métricas.
- Artefactos.
- Modelo registrado.
- Endpoint.
