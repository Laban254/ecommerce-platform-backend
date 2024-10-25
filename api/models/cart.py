# models/cart.py
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from api.models.base_model import BaseTableModel

class Cart(BaseTableModel):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    
    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
