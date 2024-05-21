from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SENDGRID_API_KEY: str
    FROM_EMAIL: str
    TO_EMAIL: str
    FRONTEND_URL: str
    BUCKET_NAME: str
    GCP_TYPE: str
    GCP_PROJECT_ID: str
    GCP_PRIVATE_KEY_ID: str
    GCP_PRIVATE_KEY: str
    GCP_CLIENT_EMAIL: str
    GCP_CLIENT_ID: str
    GCP_AUTH_URI: str
    GCP_TOKEN_URI: str
    GCP_AUTH_PROVIDER_X509_CERT_URL: str
    GCP_CLIENT_X509_CERT_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
