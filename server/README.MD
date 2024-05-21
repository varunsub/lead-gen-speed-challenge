Overview

Features
GCP Cloud Bucket File Upload
Postgres setup with SQLAlchemy ORM
API built on FastAPI

Step 1 Set up a VENV for Python

This app was built using 3.11 and it is recommended you use the same version


Use pip install -r  requiresments.txt to install the packages into the venv and run the app

Step 2 ENV setup

To run this app locally, you must use all the env vars which can be found in server/app/core/config.py or in env.example. here is a little about each env var

DATABASE_URL="URL to postgres database"
SECRET_KEY="Key for hashing passwords"
ALGORITHM="SHA256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
SENDGRID_API_KEY="API key used for sendgrid's API"
FROM_EMAIL="Email verified on Sengrid API that you will be sending from. This email is also used for test data generating purposes"
TO_EMAIL="Email of the attorney who will be contacting these leads"
FRONTEND_URL="URL of client for cors purposes"
BUCKET_NAME="Bucket path/directory for uploading the resumes/CV"
GOOGLE_APPLICATION_CREDENTIALS="Path to GCP Service key in .json file. This file should be inthe root of the server directory"


Running the app:

Run in dev using
uvicorn app.main:app --reload

This will run on localhost:8000 by default

You can then add leads by filling out the form and running the client app

You can then visit the route /login

The credentials will be the TO_EMAIL from the ENV file you set up earlier
The password will be hardcoded as password for testing purposes

Once you login successfully, you will be taken to the route /internal

This will allow you to view all your leads and mark them as contacted when the time comes