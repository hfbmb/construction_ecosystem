from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# from src.database.database import Base
from src.models.base_model import Base
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column


class ConstructionSite(Base):
    __tablename__ = "constructionsites"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
        comment="UUID",
    )
    name: Mapped[str] = mapped_column(
        String(50), comment="Name of the construction site"
    )
    description: Mapped[str] = mapped_column(
        String(255), comment="Description of the construction site"
    )
    address: Mapped[str] = mapped_column(
        String(50), comment="Address of the construction site"
    )
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    user = relationship("User", backref="constructionsites")
