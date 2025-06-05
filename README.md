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
## 💡 How It Works

1. **App Service** runs a Flask server via Gunicorn.
2. The app authenticates via `DefaultAzureCredential` (uses Managed Identity).
3. It fetches a JSON file from **Azure Blob Storage**.
4. Parses the JSON and displays person details in HTML.

## 🛠️ Deployment

- App Service Plan: `F1 (Free Tier)`
- Storage Account: `azudmzstorage97399`
- Container: `secure-data`
- Blob: `person.json`

## 🧪 Sample Output
Name: John Doe
Email: john@example.com
Role: Cloud Engineer

## Author
Chiranjeevi Podapati
