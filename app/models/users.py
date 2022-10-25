from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from core.db import BASE


class User(BASE):
    first_name = Column(String(256))
    balance = relationship("Wallet", cascade="delete")
    service = relationship("Purchase", cascade="delete")
