from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

# from src.database.database import Base
from src.models.base_model import Base
from src.common.enums import UserType


from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    username: Mapped[str] = mapped_column(String(20), default=None, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(
        String(50), comment="First name of the user"
    )
    sur_name: Mapped[str] = mapped_column(String(50), comment="Surname of the user")
    last_name: Mapped[str] = mapped_column(String(50), comment="Last name of the user")
    phone: Mapped[str] = mapped_column(
        String(11), default=False, comment="Phone number", nullable=False, unique=True
    )
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, comment="Email of the user", nullable=False
    )
    avatar: Mapped[str] = mapped_column(
        String(255), default=None, comment="Avatar of the user"
    )
    organization_name: Mapped[str] = mapped_column(
        String(50), default=None, comment="Organization name of the entity user"
    )
    bin: Mapped[str] = mapped_column(
        String(12),
        unique=True,
        index=True,
        comment="BIN of the entity user",
        nullable=False,
        default=None,
    )
    address: Mapped[str] = mapped_column(
        String(20), default=None, comment="Address of the user", nullable=False
    )
    city: Mapped[str] = mapped_column(
        String(50), default=None, comment="City of the user", nullable=False
    )
    country: Mapped[str] = mapped_column(
        String(50), default=None, comment="Country of the user", nullable=False
    )
    user_type: Mapped[str] = mapped_column(
        String(50),
        default=UserType.INDIVIDUAL,
        comment="User type either Individual or Entity",
        nullable=False,
    )
    password: Mapped[str] = mapped_column(String(255), comment="Password of the Entity")
    salt: Mapped[str] = mapped_column(String(5), comment="Encryption salt")
    role: Mapped[str] = mapped_column(String(255), comment="Role of the Entity")
    field: Mapped[str] = mapped_column(String(255), comment="Field of the Entity's role")
    website: Mapped[str] = mapped_column(String(255), comment="URL of the Entity's website")
    description: Mapped[str] = mapped_column(String(255), comment="Description of the Entity's experience")
    is_superuser: Mapped[Boolean] = mapped_column(
        Boolean, default=False, comment="Superuser privilege"
    )
    active: Mapped[Boolean] = mapped_column(
        Integer, default=True, comment="User account status"
    )
    online: Mapped[Boolean] = mapped_column(
        Integer, default=False, comment="User account status"
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, comment="When user account was created"
    )
    last_login_time: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="Last login of the user"
    )
