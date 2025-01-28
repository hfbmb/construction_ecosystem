from uuid import uuid4
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import Base
from src.common.enums import UserType


from sqlalchemy import String, Integer, DateTime
from datetime import datetime

class Response(Base):
    __tablename__ = "responses"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, comment="When user account was created"
    )
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    lot_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("lots.id"))
    user = relationship("User", backref="responses")
    lot = relationship("Lot", backref="responses")