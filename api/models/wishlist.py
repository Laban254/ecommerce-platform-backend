# api/models/wishlist.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db.database import Base

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    product_id = Column(Integer, ForeignKey("products.id"))  

    user = relationship("User", back_populates="wishlists")
    product = relationship("Product")
