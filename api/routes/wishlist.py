# api/routes/wishlist.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.services.wishlist import WishlistService
from api.schemas.product import ProductOut
from api.schemas.wishlist import WishlistItem, WishlistResponse
from typing import List

wishlist= APIRouter()

@wishlist.get("/wishlist", response_model=List[ProductOut])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    service = WishlistService(db)
    products = service.get_wishlist(user_id)
    return products

@wishlist.post("/wishlist/add", response_model=WishlistResponse)
def add_to_wishlist(item: WishlistItem, db: Session = Depends(get_db)):
    service = WishlistService(db)
    wishlist_item = service.add_to_wishlist(item.user_id, item.product_id)
    return {"id": wishlist_item.id, "user_id": wishlist_item.user_id, "product_id": wishlist_item.product_id}

@wishlist.delete("/wishlist/remove/{product_id}")
def remove_from_wishlist(product_id: int, user_id: int, db: Session = Depends(get_db)):
    service = WishlistService(db)
    message = service.remove_from_wishlist(user_id, product_id)
    return message
