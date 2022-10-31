from schemas import Base

from enum import Enum


class Name(str, Enum):
    THREE_DAYS = "Продвижение на 3 дня"
    TEN_DAYS = "Продвижение на 10 дней"
    MOUNTH = "Продвижение на месяц"


class Service(Base):
    name: Name
    price: float
