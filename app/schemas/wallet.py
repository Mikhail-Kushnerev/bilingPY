from pydantic import Field

from schemas import Base


class GetWallet(Base):

    money: float = Field(
        ...,
        alias="balance",
        title="Баланс",
        description="Оставшиеся деньги у пользователя"
    )


class CreateWallet(Base):

    wallet: float = Field(
        ...,
        ge=10.,
        le=150.,
        alias="balance",
        title="Деньги на покупку",
        description="Деньги на резерв для предоставления услуги"
    )
