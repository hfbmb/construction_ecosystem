from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import ForeignKey, Integer, String, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# from src.database.database import Base
from src.models.base_model import Base


class Lot(Base):
    __tablename__ = "lots"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    title: Mapped[str] = mapped_column(String(50), comment="Title of the lot")
    description: Mapped[str] = mapped_column(
        String(255), comment="Description of the lot"
    )
    fromTime: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, comment="From time of the lot"
    )
    toTime: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, comment="To time of the lot"
    )
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    user = relationship("User", backref="lots")
