from fastapi import FastAPI
from src.config.project_config import settings
from src.api.routers import v1


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        openapi_prefix=settings.OPENAPI_PREFIX,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL,
    )

    register_router(app)

    return app


def register_router(app: FastAPI):
    app.include_router(v1)
