from sqlalchemy.ext.asyncio import AsyncSession

from crud import Base
from models import Purchase
from schemas.purchase import CreatePurchase


class PurchaseCRUD(Base):

    async def get(
            self,
            session: AsyncSession,
            data: CreatePurchase
    ):
        purchase = Purchase(**data.dict())
        session.add(purchase)
        await session.commit()
        await session.refresh(purchase)
        return purchase


users_crud = PurchaseCRUD(Purchase)
