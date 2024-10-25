# routes/cart.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.models.cart import Cart
from api.models.user import User
from api.schemas.cart import CartItemCreate, CartItemResponse
from api.services.user import user_service
from api.services.cart import view_cart, add_to_cart, remove_from_cart, clear_cart

cart = APIRouter(tags=["Cart"])

@cart.get("/cart", response_model=list[CartItemResponse])
async def get_cart(user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    """
    View the current user's cart.
    """
    return view_cart(user.id, db)

@cart.post("/cart/add", response_model=CartItemResponse)
async def add_cart_item(cart_item: CartItemCreate, user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    """
    Add a product to the cart.
    """
    return add_to_cart(cart_item, user.id, db)

@cart.delete("/cart/remove/{product_id}")
async def remove_cart_item(product_id: int, user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    """
    Remove a product from the cart.
    """
    return remove_from_cart(product_id, user.id, db)

@cart.delete("/cart/clear")
async def clear_cart_items(user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    """
    Clear all items from the user's cart.
    """
    return clear_cart(user.id, db)

