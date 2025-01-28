from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.project_schema import ProjectCreate, ProjectUpdate

from src.models.project_model import User
# from src.database.database import get_db


class ProjectRepository(SqlAlchemyRepository[ModelType, ProjectCreate, ProjectUpdate]):
    pass
