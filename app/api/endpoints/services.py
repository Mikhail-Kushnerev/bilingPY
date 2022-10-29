from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import services_crud
from schemas import Service


services_router = APIRouter()


@services_router.post(
    "/add-service"
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
