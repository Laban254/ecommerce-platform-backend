# models/review.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_model import BaseTableModel

class Review(BaseTableModel):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

    product = relationship("Product", back_populates="reviews")
    user = relationship("User", back_populates="reviews")  

    def __repr__(self):
        return f"<Review(product_id={self.product_id}, user_id={self.user_id}, rating={self.rating}, comment={self.comment})>"
