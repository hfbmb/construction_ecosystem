from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.category_schema import CategoryCreate, CategoryUpdate

from src.models.category_model import Category
from src.database.database import get_db


class CategoryRepository(SqlAlchemyRepository[ModelType, CategoryCreate, CategoryUpdate]):
    pass
