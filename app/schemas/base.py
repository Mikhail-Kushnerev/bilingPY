from pydantic import BaseModel


class Base(BaseModel):

    id: int

    class Config:
        orm_mode = True
