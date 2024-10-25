# schemas/review.py
from pydantic import BaseModel
from typing import Optional

class ReviewCreate(BaseModel):
    rating: int
    comment: Optional[str] = None

class ReviewResponse(ReviewCreate):
    id: int
    product_id: int
    user_id: int

    class Config:
        orm_mode = True
