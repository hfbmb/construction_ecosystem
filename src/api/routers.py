from fastapi import APIRouter

from src.api.v1.user import router as user_router

v1 = APIRouter(prefix="/v1")

v1.include_router(user_router, prefix="/user", tags=["user"])
