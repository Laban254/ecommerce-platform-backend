# models/product.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from api.models.base_model import BaseTableModel
from sqlalchemy.orm import relationship



class Product(BaseTableModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    cart_items = relationship("Cart", back_populates="product")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, is_active={self.is_active})>"
