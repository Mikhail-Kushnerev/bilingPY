from pydantic import BaseModel


class CreatePurchase(BaseModel):
    user_id: int
    service_id: int
    price: int
