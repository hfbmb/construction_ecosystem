from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.review_schema import ReviewCreate, ReviewUpdate

from src.models.review_model import Review
# from src.database.database import get_db


class ReviewsRepository(SqlAlchemyRepository[ModelType, ReviewCreate, ReviewUpdate]):
    pass