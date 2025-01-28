from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from typing import Generator

from contextlib import asynccontextmanager

from src.config.db_config import settings_db

engine = create_async_engine(settings_db.database_url, future=True, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# @lru_cache
# async def create_session() -> AsyncSession:
#     async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
#     return async_session


@asynccontextmanager
async def get_db() -> Generator[AsyncSession, None, None]:
    from sqlalchemy import exc

    session: AsyncSession = async_session()
    try:
        yield session
    except exc.SQLAlchemyError as error:
        await session.rollback()
        raise error
    finally:
        await session.close()


# Base = declarative_base()
