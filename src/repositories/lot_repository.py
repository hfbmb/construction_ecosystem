from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.schemas.lot_schema import LotCreate, LotUpdate

from src.models.lot_model import Lot
# from src.database.database import get_db


class LotRepository(SqlAlchemyRepository[ModelType, LotCreate, LotUpdate]):
    pass
