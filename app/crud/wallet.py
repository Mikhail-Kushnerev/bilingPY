from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from crud import Base
from models import Wallet


class WalletCRUD(Base):

    async def check_balance(
            self,
            user_id: int,
            session: AsyncSession
    ):
        obj = await session.execute(
            select(Wallet.money).where(
                Wallet.user_id == user_id
            )
        )
        return obj.scalars().first()

    async def send_money(
        self,
        money: float,
        session: AsyncSession
    ):
        db_data = await session.execute(
            select(Wallet)
            .where(
                Wallet.id == 1
            )
        )
        db_data = db_data.scalars().first()
        db_data.money += money
        session.add(db_data)
        await session.commit()
        return db_data


wallet_crud = WalletCRUD(Wallet)
