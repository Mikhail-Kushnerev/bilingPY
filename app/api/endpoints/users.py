from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import users_crud, wallet_crud
from schemas import CreateUser
from validators import check_exists_user


user_router = APIRouter()


@user_router.post(
    "/sign-up"
)
async def create_user(
        person: CreateUser,
        session: AsyncSession = Depends(get_async_session)
) -> str:
    await check_exists_user(person.id, session)
    await users_crud.create(
        person,
        session
    )
    return "Done!"


@user_router.post(
    "/"
)
async def send_money_from_user_to_user(

):
    ...
