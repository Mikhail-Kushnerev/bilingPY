from sqlalchemy import Column, String, Float

from core.db import BASE


class Service(BASE):
    name = Column(String)
    price = Column(Float)
