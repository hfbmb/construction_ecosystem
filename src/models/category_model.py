from sqlalchemy import String, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

# from src.database.database import Base
from src.models.base_model import Base
from uuid import uuid4


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
        comment="UUID",
    )
    name: Mapped[str] = mapped_column(String(50), comment="Name of the category")
