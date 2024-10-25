from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from api.models.base_model import BaseTableModel

class OrderItem(BaseTableModel):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  

    order = relationship("Order", back_populates="items")
    product = relationship("Product")
