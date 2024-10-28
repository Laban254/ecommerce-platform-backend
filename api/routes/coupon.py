# api/routes/coupon.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.schemas.coupon import CouponCreate, CouponResponse
from api.services.coupon import CouponService

coupon = APIRouter()

@coupon.post("/apply-coupon", response_model=CouponResponse)
def apply_coupon(code: str, db: Session = Depends(get_db)):
    service = CouponService(db)
    coupon = service.apply_coupon(code)
    return {
        "id": coupon.id,
        "code": coupon.code,
        "discount_percentage": coupon.discount_percentage,
        "expiry_date": coupon.expiry_date,
    }
