param([string]$RESOURCE_GROUP = "rg-mlops-taller3")
az group delete --name $RESOURCE_GROUP --yes --no-wait
