# api/models/coupon.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from api.db.database import Base
from datetime import datetime

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount_percentage = Column(Float, nullable=False)
    expiry_date = Column(DateTime, nullable=False)

    def is_valid(self) -> bool:
        return self.expiry_date > datetime.now()
