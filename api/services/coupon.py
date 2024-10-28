# api/services/coupon.py

from sqlalchemy.orm import Session
from api.models.coupon import Coupon
from api.schemas.coupon import CouponCreate
from fastapi import HTTPException

class CouponService:
    def __init__(self, db: Session):
        self.db = db

    def create_coupon(self, coupon: CouponCreate):
        db_coupon = Coupon(**coupon.dict())
        self.db.add(db_coupon)
        self.db.commit()
        self.db.refresh(db_coupon)
        return db_coupon

    def apply_coupon(self, code: str):
        coupon = self.db.query(Coupon).filter(Coupon.code == code).first()
        if not coupon or not coupon.is_valid():
            raise HTTPException(status_code=400, detail="Invalid or expired coupon")
        return coupon
