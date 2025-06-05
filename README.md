# Secure Flask App on Azure using Terraform

This project demonstrates how to deploy a Flask web application to Azure App Service using Terraform.

## Features
- Flask app hosted on Azure App Service (Linux, Python 3.9)
- Blob Storage integration using `azure-identity` and `azure-storage-blob`
- Terraform used to provision infrastructure
- Custom `startup.sh` to resolve dependency issues

## Steps
1. Wrote a Flask app that pulls JSON data from Azure Blob
2. Packaged code into `app.zip`
3. Provisioned Azure resources with Terraform
4. Encountered `ModuleNotFoundError` for Azure packages
5. Resolved using custom `startup.sh` to pip install dependencies
6. Successfully deployed via `az webapp deploy`

## Author
Chiranjeevi Podapati
