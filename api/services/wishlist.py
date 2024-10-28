# api/services/wishlist.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.wishlist import Wishlist
from api.models.product import Product

class WishlistService:
    def __init__(self, db: Session):
        self.db = db

    def get_wishlist(self, user_id: int):
        wishlists = self.db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
        product_ids = [wishlist.product_id for wishlist in wishlists]
        products = self.db.query(Product).filter(Product.id.in_(product_ids)).all()
        return products

    def add_to_wishlist(self, user_id: int, product_id: int):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        existing_wishlist_item = self.db.query(Wishlist).filter(
            Wishlist.user_id == user_id,
            Wishlist.product_id == product_id
        ).first()
        if existing_wishlist_item:
            raise HTTPException(status_code=400, detail="Product already in wishlist")

        wishlist_item = Wishlist(user_id=user_id, product_id=product_id)
        self.db.add(wishlist_item)
        self.db.commit()
        self.db.refresh(wishlist_item)
        return wishlist_item

    def remove_from_wishlist(self, user_id: int, product_id: int):
        wishlist_item = self.db.query(Wishlist).filter(
            Wishlist.user_id == user_id,
            Wishlist.product_id == product_id
        ).first()
        if not wishlist_item:
            raise HTTPException(status_code=404, detail="Wishlist item not found")

        self.db.delete(wishlist_item)
        self.db.commit()
        return {"message": "Product removed from wishlist"}
