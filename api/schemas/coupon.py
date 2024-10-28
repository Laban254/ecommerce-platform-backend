# api/schemas/coupon.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CouponCreate(BaseModel):
    code: str
    discount_percentage: float
    expiry_date: datetime

class CouponResponse(BaseModel):
    id: int
    code: str
    discount_percentage: float
    expiry_date: datetime

    class Config:
        orm_mode = True
