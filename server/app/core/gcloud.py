import os
from google.cloud import storage
from google.oauth2 import service_account


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    try:
        # Construct the credentials from environment variables
        credentials_info = {
            "type": os.environ["GCP_TYPE"],
            "project_id": os.environ["GCP_PROJECT_ID"],
            "private_key_id": os.environ["GCP_PRIVATE_KEY_ID"],
            "private_key": os.environ["GCP_PRIVATE_KEY"].replace("\\n", "\n"),
            "client_email": os.environ["GCP_CLIENT_EMAIL"],
            "client_id": os.environ["GCP_CLIENT_ID"],
            "auth_uri": os.environ["GCP_AUTH_URI"],
            "token_uri": os.environ["GCP_TOKEN_URI"],
            "auth_provider_x509_cert_url": os.environ[
                "GCP_AUTH_PROVIDER_X509_CERT_URL"
            ],
            "client_x509_cert_url": os.environ["GCP_CLIENT_X509_CERT_URL"],
        }

        credentials = service_account.Credentials.from_service_account_info(
            credentials_info
        )

        storage_client = storage.Client(
            credentials=credentials, project=os.environ["GCP_PROJECT_ID"]
        )
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        return blob.public_url
    except Exception as e:
        print(e)
        return ""
