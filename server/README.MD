# Overview

## Features

- **GCP Cloud Bucket File Upload**
- **Postgres setup with SQLAlchemy ORM**
- **API built on FastAPI**
- **Sengrid for Email Sending**
- **Next.js Frontend**


## Step 1: Set up a VENV for Python

This app was built using Python 3.11 and it is recommended you use the same version.

1. Create a virtual environment:
   ```bash
   python3.11 -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Step 2: ENV Setup

To run this app locally, you must use all the environment variables (env vars) which can be found in `server/app/core/config.py` or in `env.example`. Here is a little about each env var:

- `DATABASE_URL`: URL to the Postgres database
- `SECRET_KEY`: Key for hashing passwords
- `ALGORITHM`: SHA256
- `ACCESS_TOKEN_EXPIRE_MINUTES`: 30
- `SENDGRID_API_KEY`: API key used for SendGrid's API
- `FROM_EMAIL`: Email verified on SendGrid API that you will be sending from. This email is also used for test data generating purposes
- `TO_EMAIL`: Email of the attorney who will be contacting these leads
- `FRONTEND_URL`: URL of the client for CORS purposes
- `BUCKET_NAME`: Bucket path/directory for uploading the resumes/CV


## Running the App

Navigate to the server directory from the root
```bash
cd ./server
```

Run in development mode using:
```bash
uvicorn app.main:app --reload
```
This will run on `localhost:8000` by default.

### Adding Leads

You can then add leads by filling out the form and running the client app.

### Login

You can visit the route `/login`.

- **Credentials:**
  - **Email**: The `TO_EMAIL` from the ENV file you set up earlier
  - **Password**: `password` (hardcoded for testing purposes)

### Internal Route

Once you log in successfully, you will be taken to the route `/internal`.

This will allow you to view all your leads and mark them as contacted when the time comes.

## Additional Details

Make sure to replace placeholders in the example `.env` file with actual values.

Here is an example `.env` file:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
ALGORITHM=SHA256
ACCESS_TOKEN_EXPIRE_MINUTES=30
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_verified_email@example.com
TO_EMAIL=attorney_email@example.com
FRONTEND_URL=http://localhost:3000
BUCKET_NAME=your_bucket_name
GCP_TYPE="service_account"
GCP_PROJECT_ID="your-project-id"
GCP_PRIVATE_KEY_ID="your-private-key-id"
GCP_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nyour-private-key\n-----END PRIVATE KEY-----\n"
GCP_CLIENT_EMAIL="your-service-account-email@your-project-id.iam.gserviceaccount.com"
GCP_CLIENT_ID="your-client-id"
GCP_AUTH_URI="https://accounts.google.com/o/oauth2/auth"
GCP_TOKEN_URI="https://oauth2.googleapis.com/token"
GCP_AUTH_PROVIDER_X509_CERT_URL="https://www.googleapis.com/oauth2/v1/certs"
GCP_CLIENT_X509_CERT_URL="https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email%40your-project-id.iam.gserviceaccount.com"
```

With these steps, you should be able to set up, run, and test the application locally.
