from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from typing import Annotated

# id_key = Annotated[
#     int, mapped_column(primary_key=True, index=True, autoincrement=True, sort_order=-999, comment='primary key')
# ]


class Base(DeclarativeBase):
    # __abstract__ = True
    pass
    # id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True, sort_order=-999, comment='primary key')
    # created_at: Mapped[datetime] = mapped_column(default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(
    #     TIMESTAMP(timezone=True),
    #     default=func.now(),
    #     onupdate=func.now()
    # )

    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return f"{cls.__name__.lower()}"
