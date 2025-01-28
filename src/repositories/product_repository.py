from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.product_schema import ProductCreate, ProductUpdate

from src.models.product_model import Product
from src.database.database import get_db


class ProductRepository(SqlAlchemyRepository[ModelType, ProductCreate, ProductUpdate]):
    pass
