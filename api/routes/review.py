# routes/review.py
from fastapi import APIRouter, Depends, List
from sqlalchemy.orm import Session
from api.db.database import get_db  # Adjust the import based on your database session function
from api.schemas.review import ReviewCreate, ReviewResponse  # Create these schemas
from api.services.review import ReviewService
from api.services.user import user_service
from api.models.user import User

review = APIRouter(tags=["Review"])

@review.post("/products/{product_id}/reviews", response_model=ReviewResponse)
async def create_review(product_id: int, review: ReviewCreate, db: Session = Depends(get_db), current_user: User = Depends(user_service.get_current_user)):
    review_service = ReviewService(db)
    new_review = review_service.create_review(product_id=product_id, user_id=current_user.id, review=review)
    return new_review


@review.get("/products/{product_id}/reviews", response_model=List[ReviewResponse])
async def get_reviews(product_id: int, db: Session = Depends(get_db)):
    review_service = ReviewService(db)
    reviews = review_service.get_reviews(product_id=product_id)
    return reviews
