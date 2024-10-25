# services/review.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.review import Review
from api.models.product import Product
from api.schemas.review import ReviewCreate

class ReviewService:
    def __init__(self, db: Session):
        self.db = db

    def create_review(self, product_id: int, user_id: int, review: ReviewCreate):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        new_review = Review(product_id=product_id, user_id=user_id, **review.dict())
        self.db.add(new_review)
        self.db.commit()
        self.db.refresh(new_review)
        return new_review

    def get_reviews(self, product_id: int):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        reviews = self.db.query(Review).filter(Review.product_id == product_id).all()
        return reviews
