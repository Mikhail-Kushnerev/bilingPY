from sqlalchemy import (
    Integer,
    Float,
    Column,
    String
)
from sqlalchemy.orm import relationship

from core.db import BASE


class User(BASE):
    telegram_id = Column(Integer)
    first_name = Column(String(256))
    last_name = Column(String(256))
    wallet = Column(Float)
    purchase = relationship(
        "Purchase",
        cascade="delete"
    )
    event = relationship(
        "Event",
        cascade="delete"
    )
