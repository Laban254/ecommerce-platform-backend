# api/routes/order.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.models.user import User
from api.schemas.order import OrderResponse, OrderUpdate
from api.services.order import list_orders, view_order, update_order_status
from api.services.user import user_service

order_router = APIRouter(tags=["Order"])

@order_router.get("/orders", response_model=list[OrderResponse])
async def get_orders(user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    return list_orders(user.id, db)

@order_router.get("/orders/{id}", response_model=OrderResponse)
async def get_order(id: int, user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    return view_order(id, user.id, db)

@order_router.patch("/orders/{id}", response_model=OrderResponse)
async def patch_order(id: int, order_update: OrderUpdate, user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    return update_order_status(id, order_update, user.id, db)
