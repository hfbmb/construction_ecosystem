from src.schemas.base_schema import PyModel
from src.repositories.sqlalchemy_repository import ModelType
from sqlalchemy.dialects.postgresql import UUID
from src.repositories.base_repository import AbstractRepository


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data=model.model_dump())

    async def update(self, pk: int, model: PyModel) -> ModelType:
        return await self.repository.update(data=model.model_dump(), id=pk)

    async def delete(self, filters):
        return await self.repository.delete(**filters)

    async def get(self, pk: UUID = None) -> ModelType:
        if pk:
            return await self.repository.get_single(id=pk)
        return await self.repository.get_multi()
