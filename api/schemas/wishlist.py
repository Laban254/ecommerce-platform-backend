# api/schemas/wishlist.py

from pydantic import BaseModel

class WishlistItem(BaseModel):
    user_id: int
    product_id: int

class WishlistResponse(BaseModel):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True
