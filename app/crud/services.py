from sqlalchemy.ext.asyncio import AsyncSession # noqa

from crud import Base
from models import Service


class ServicesClass(Base):

    def get(self):
        return self


services_crud = ServicesClass(Service)
