from sqlalchemy.ext.asyncio import AsyncSession

from crud import Base
from models import User
from schemas import CreateUser


class UserCRUD(Base):

    async def send(
            self,
            session: AsyncSession,
            user: CreateUser
    ):
        user = User(**user.dict(exclude_none=True))
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


users_crud = UserCRUD(User)
