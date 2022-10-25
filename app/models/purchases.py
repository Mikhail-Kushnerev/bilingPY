from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from core.db import BASE


class Purchase(BASE):
    user_id = Column(Integer, ForeignKey("user.id"))
    service = Column(String)
    data = Column(DateTime)
