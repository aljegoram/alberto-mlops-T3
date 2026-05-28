param(
    [string]$RESOURCE_GROUP = "rg-mlops-taller3",
    [string]$WORKSPACE = "aml-mlops-taller3"
)

az configure --defaults group=$RESOURCE_GROUP workspace=$WORKSPACE
az ml job create --file azureml/train-job.yml --stream
