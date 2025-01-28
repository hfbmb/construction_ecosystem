from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.constructionsite_schema import ConstructionsiteCreate, ConstructionsiteUpdate

from src.models.constructionsite_model import ConstructionSite
from src.database.database import get_db


class ConstructionsiteRepository(SqlAlchemyRepository[ModelType, ConstructionsiteCreate, ConstructionsiteUpdate]):
    pass
