from typing import Optional

from pydantic import Field

from schemas import Base


class CreateUser(Base):
    telegram_id: int = Field(
        ...,
        title="id пользователя Telegram"
    )
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=256,
        title="Имя пользователя"
    )
    last_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=256,
        title="Имя пользователя"
    )


class UpdateUser(Base):
    pass
