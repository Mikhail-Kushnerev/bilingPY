from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.users import BalanceRead


class UserCRUD():

    async def create(
            self,
            session: AsyncSession,
            user: BalanceRead
    ):
        user = User(**user.dict())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


users_crud = UserCRUD()
