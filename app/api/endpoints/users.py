from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import users_crud
from models import User
from schemas import BalanceRead


router = APIRouter()


@router.post(
    "/my",
)
async def send_balance(
        person: BalanceRead,
        session: AsyncSession = Depends(get_async_session)
) -> User:
    return await users_crud.create(
        session,
        person
    )
