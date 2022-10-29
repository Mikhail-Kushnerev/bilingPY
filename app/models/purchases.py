from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from core.db import BASE


class Purchase(BASE):
    user_id = Column(Integer, ForeignKey("user.id"))
    service_id = Column(Integer, ForeignKey("service.id"))
    price = Column(Integer)
    data = Column(DateTime)
