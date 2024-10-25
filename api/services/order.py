# api/services/order
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.models.order import Order
from api.schemas.order import OrderResponse, OrderUpdate

def list_orders(user_id: int, db: Session) -> list[OrderResponse]:
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders

def view_order(order_id: int, user_id: int, db: Session) -> OrderResponse:
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def update_order_status(order_id: int, order_update: OrderUpdate, user_id: int, db: Session) -> OrderResponse:
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # todo: check if the user is an admin. Implement this check based on your logic
    if not user_is_admin(user_id):  # Replace with actual admin check
        raise HTTPException(status_code=403, detail="Not authorized to update order status")

    order.status = order_update.status
    db.commit()
    db.refresh(order)
    return order

def user_is_admin(user_id: int) -> bool:
    # todo: Implement your logic to check if the user is an admin
    return True  # Placeholder, replace with actual logic
