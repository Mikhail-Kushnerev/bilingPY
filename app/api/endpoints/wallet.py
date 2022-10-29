from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import wallet_crud

wallet_router = APIRouter()


@wallet_router.get(
    "/my-balance"
)
async def check_balance(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> int:
    result = await wallet_crud.check_balance(
        user_id,
        session
    )
    return result


@wallet_router.post(
    "/send-money"
)
async def send_money(
        user: int,
        money: float,
        session: AsyncSession = Depends(get_async_session)
):
    result = await wallet_crud.check_balance(
        user,
        session
    )
    if result and result > 0:
        return await wallet_crud.send_money(
            money,
            session
        )
