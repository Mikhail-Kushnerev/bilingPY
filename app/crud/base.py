from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Wallet


class Base:

    def __init__(self, model):
        self.model = model

    async def get(
            self,
            data: int,
            session: AsyncSession
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == data
            )
        )
        return db_obj.scalars().first()

    async def create(
            self,
            data,
            session: AsyncSession,
    ):
        item = self.model(**data.dict())
        wallet = Wallet(user_id=data.id, money=0)
        session.add(item)
        session.add(wallet)
        await session.commit()
