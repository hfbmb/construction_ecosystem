from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.database import async_session, get_db
from src.schemas.user_schema import Individual, ShowIndividual, ShowEntity, Entity, UserSchema
from src.services.user_service import UserService
from src.dependencies.user_dependency import get_user_service

router = APIRouter(prefix='/user', tags=['user'])


# , response_model=ShowIndividual
@router.post("/individual")
async def create_individual(
    body: Individual, user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.create(body)


# , response_model=ShowEntity
@router.post("/entity")
async def create_entity(
    body: Entity, user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.create(body)


@router.post("/login", response_model=UserSchema)
async def login(
    user_service: Annotated[UserService, Depends(get_user_service)],
    payload: OAuth2PasswordRequestForm = Depends(),
) -> UserSchema:
    # exception handler
    res = await user_service.get({"username": payload.username})
    return res


@router.delete("/delete/{username}")
async def delete_user(
    username: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    res = await user_service.delete({"username": username})
    return res
