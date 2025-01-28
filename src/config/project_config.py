from dotenv import load_dotenv
import os

load_dotenv(".env")


class Settings:
    DB_ECHO: bool = True
    TITLE: str = os.environ.get("TITLE")
    DESCRIPTION: str = os.environ.get("DESCRIPTION")
    VERSION: str = "1.0.0"
    DEBUG: bool = os.environ.get("DEBUG")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    CORS_ALLOWED_ORIGINS: str = os.environ.get("CORS_ALLOWED_ORIGINS")
    OPENAPI_PREFIX: str = os.environ.get("OPENAPI_PREFIX")
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/api"


settings = Settings()
