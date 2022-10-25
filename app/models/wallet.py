from sqlalchemy import (
    Column,
    Float,
    Integer,
    ForeignKey
)

from core.db import BASE


class Wallet(BASE):
    user_id = Column(Integer, ForeignKey("user.id"))
    money = Column(Float)
