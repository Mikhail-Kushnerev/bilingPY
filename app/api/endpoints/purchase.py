from redis import Redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_async_session, get_cache
from crud import PurchaseCRUD
from schemas import CreatePurchase


purchase_router = APIRouter()


@purchase_router.post("/buy")
async def make_purchase(
        data: CreatePurchase,
        cart: Redis = Depends(get_cache),
        session: AsyncSession = Depends(get_async_session)
):
    datas = await PurchaseCRUD.create(session, data)
    return datas.dict()
