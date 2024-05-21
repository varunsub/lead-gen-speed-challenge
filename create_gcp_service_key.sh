#!/bin/bash

echo "Creating GCP service key JSON file..."

# Check current directory
echo "Current directory: $(pwd)"

# Create the directory if it doesn't exist
mkdir -p /server

# Verify if the directory was created
if [ -d /server ]; then
  echo "/server directory exists or was successfully created."
else
  echo "Failed to create /server directory."
  exit 1
fi

cat <<EOF > /server/credentials.json
{
  "type": "${GCP_TYPE}",
  "project_id": "${GCP_PROJECT_ID}",
  "private_key_id": "${GCP_PRIVATE_KEY_ID}",
  "private_key": "${GCP_PRIVATE_KEY}",
  "client_email": "${GCP_CLIENT_EMAIL}",
  "client_id": "${GCP_CLIENT_ID}",
  "auth_uri": "${GCP_AUTH_URI}",
  "token_uri": "${GCP_TOKEN_URI}",
  "auth_provider_x509_cert_url": "${GCP_AUTH_PROVIDER_X509_CERT_URL}",
  "client_x509_cert_url": "${GCP_CLIENT_X509_CERT_URL}"
}
EOF

# Check if the file was created
if [ -f /server/credentials.json ]; then
  echo "GCP service key JSON file created at /server/credentials.json"
else
  echo "Failed to create GCP service key JSON file."
fi
