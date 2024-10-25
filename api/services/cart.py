# api/services/cart.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from api.models.cart import Cart
from api.models.product import Product
from api.models.user import User
from api.schemas.cart import CartItemCreate

def view_cart(user_id: str, db: Session):
    """
    View the current user's cart.
    """
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    return cart_items

def add_to_cart(cart_item: CartItemCreate, user_id: str, db: Session):
    """
    Add a product to the cart or update its quantity if it already exists.
    """
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    existing_cart_item = db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == cart_item.product_id).first()
    
    if existing_cart_item:
        existing_cart_item.quantity += cart_item.quantity
        db.commit()  
        db.refresh(existing_cart_item) 
        return existing_cart_item  
    else:
        new_cart_item = Cart(user_id=user_id, product_id=cart_item.product_id, quantity=cart_item.quantity)
        db.add(new_cart_item)
        db.commit()
        db.refresh(new_cart_item)
        return new_cart_item

def remove_from_cart(product_id: int, user_id: str, db: Session):
    """
    Remove a product from the cart.
    """
    cart_item = db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found in cart")
    
    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

def clear_cart(user_id: str, db: Session):
    """
    Clear all items from the user's cart.
    """
    db.query(Cart).filter(Cart.user_id == user_id).delete()
    db.commit()
    return {"message": "All items removed from cart"}
