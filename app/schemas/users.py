from pydantic import Field

from schemas import Base


class CreateUser(Base):

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=256,
        title="Имя пользователя"
    )


class UpdateUser(Base):
    pass
