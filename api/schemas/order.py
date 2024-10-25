# schemas/order.py
from pydantic import BaseModel

class OrderResponse(BaseModel):
    id: int
    total_amount: float
    status: str

    class Config:
        orm_mode = True
class OrderUpdate(BaseModel):
    status: str