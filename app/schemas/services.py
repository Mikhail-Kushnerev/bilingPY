from enum import Enum


class Service(str, Enum):
    THREE_DAYS = "Продвижение на 3 дня"
    TEN_DAYS = "Продвижение на 10 дней"
    MOUNTH = "Продвижение на месяц"
