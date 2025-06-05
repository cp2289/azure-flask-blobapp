from flask import Flask, render_template_string
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient
import json

app = Flask(__name__)

@app.route("/")
def show_person_info():
    try:
        # Authenticate with Azure Managed Identity
        credential = DefaultAzureCredential()

        # Connect to the blob
        blob_client = BlobClient(
            account_url="https://azudmzstorage97399.blob.core.windows.net",
            container_name="secure-data",
            blob_name="person.json",
            credential=credential
        )

        # Download and decode the JSON data
        blob_data = blob_client.download_blob().readall()
        person_info = json.loads(blob_data.decode('utf-8'))

        # Define the HTML to render
        html = """
        <h2>Person Information</h2>
        <ul>
            <li><strong>Name:</strong> {{ name }}</li>
            <li><strong>Email:</strong> {{ email }}</li>
            <li><strong>Role:</strong> {{ role }}</li>
        </ul>
        """

        return render_template_string(
            html,
            name=person_info.get("name", "N/A"),
            email=person_info.get("email", "N/A"),
            role=person_info.get("role", "N/A")
        )

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

# Optional for local run
if __name__ == "__main__":
    app.run(debug=True)

