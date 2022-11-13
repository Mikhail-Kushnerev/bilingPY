from core import BASE

from sqlalchemy import Column, String, ForeignKey, Integer


class Event(BASE):
    user_id = Column(Integer, ForeignKey("user.id"))
    command = Column(String(256))
