from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings

BASE = declarative_base()

engine = create_async_engine(settings.database_url())


async def get_async_session() -> AsyncSession:
    AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
    async with AsyncSessionLocal() as async_session:
        yield async_session
