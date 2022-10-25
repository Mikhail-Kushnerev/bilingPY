from pydantic import BaseModel

from .services import Service


class Base(BaseModel):
    id: int


class BalanceRead(Base):
    first_name: str
    balance: int


class MoneySend(Base):
    money: float
    service: Service


class BalanceUpdate(Base):
    money: float
