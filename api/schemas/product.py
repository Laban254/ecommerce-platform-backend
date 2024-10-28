# schemas/product.py
from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_active: bool

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    id: int
    name: str
    category: str
    price: float
    description: str  # Add other fields as necessary

    class Config:
        orm_mode = True
