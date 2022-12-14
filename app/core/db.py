from redis import Redis
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr

from core import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


BASE = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url())


async def get_async_session() -> AsyncSession:
    AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
    async with AsyncSessionLocal() as async_session:
        yield async_session


redis_client = Redis(
    host="cache",
    port=6379,
    db=0
)


def get_cache() -> Redis:
    with redis_client as redis:
        yield redis

