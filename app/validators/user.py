from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud.users import users_crud


async def check_exists_user(
        preson_id: int,
        session: AsyncSession
) -> None:
    result = await users_crud.get(preson_id, session)
    if result:
        raise HTTPException(
            status_code=422,
            detail=str(result)
        )
