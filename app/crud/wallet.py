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
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        target = await session.execute(
            update(Wallet)
            .where(
                Wallet.id == 1
            )
            .values(
                {"money": (Wallet.money + money)}
            )
        )
        # session.add(target)
        await session.commit()
        return target


wallet_crud = WalletCRUD(Wallet)
