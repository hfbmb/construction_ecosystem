from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.models.base_model import Base

# from src.database.database import Base
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    user = relationship("User", backref="projects")
    address: Mapped[str] = mapped_column(String(20), comment="Address of the project")
    description: Mapped[str] = mapped_column(
        String(255), comment="Description of the project"
    )
