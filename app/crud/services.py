from redis import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from crud import Base
from models import Service, Purchase


class ServicesClass(Base):

    async def add_to_cart(
        self,
        service: int,
        user: int,
        session: Redis
    ):
        session.set(name=user, value=service)


services_crud = ServicesClass(Service)
