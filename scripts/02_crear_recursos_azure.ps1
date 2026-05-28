param(
    [string]$RESOURCE_GROUP = "rg-mlops-taller3",
    [string]$LOCATION = "eastus",
    [string]$WORKSPACE = "aml-mlops-taller3",
    [string]$COMPUTE = "cpu-cluster"
)

az group create --name $RESOURCE_GROUP --location $LOCATION

az ml workspace create --name $WORKSPACE --resource-group $RESOURCE_GROUP --location $LOCATION

az configure --defaults group=$RESOURCE_GROUP workspace=$WORKSPACE location=$LOCATION

az ml compute create --name $COMPUTE --type amlcompute --size STANDARD_DS3_V2 --min-instances 0 --max-instances 1
