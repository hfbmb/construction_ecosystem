from sqlalchemy import ForeignKey, Integer, String, Float, Boolean, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from uuid import uuid4

# from src.database.database import Base
from src.models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(50), comment="Name of the product")
    description: Mapped[str] = mapped_column(
        String(255), comment="Description of the product"
    )
    address: Mapped[str] = mapped_column(String(50), comment="Address of the product")
    price: Mapped[Float] = mapped_column(Float, comment="Price of the product")
    isnegotiable: Mapped[Boolean] = mapped_column(
        Boolean, comment="Whether the product is negotiable"
    )
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    user = relationship("User", backref="products")
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("categories.id"))
