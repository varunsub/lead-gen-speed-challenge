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
    GOOGLE_APPLICATION_CREDENTIALS: str

    class Config:
        env_file = ".env"


settings = Settings()
