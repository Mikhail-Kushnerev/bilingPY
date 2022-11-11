from redis import Redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_async_session, get_cache
from crud import services_crud
from schemas import Service


services_router = APIRouter()


@services_router.post(
    "/add-service",
    # response_model=Service
)
async def create_new_service(
        data: Service,
        session: AsyncSession = Depends(get_async_session)
):
    result = await services_crud.create(
        data,
        session
    )
    return result


@services_router.post(
    "/add-to-cart"
)
async def choice_service(
        service_id: int,
        user_id: int,
        cache: Redis = Depends(get_cache)
):
    await services_crud.add_to_cart(
        service_id,
        user_id,
        cache
    )
    return {"Добавлено!"}
