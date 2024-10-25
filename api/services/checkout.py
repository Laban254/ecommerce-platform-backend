from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models.order import Order
from api.models.order_item import OrderItem
from api.models.cart import Cart
from api.models.product import Product

def process_checkout(user_id: int, db: Session):
    with db.begin():
        # Retrieve user's cart items
        cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()

        if not cart_items:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")

        total_amount = 0

        # Check product availability and calculate total amount
        for item in cart_items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {item.product_id} not found")
            if product.stock < item.quantity:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not enough stock for product {product.name}")
            total_amount += item.quantity * product.price

        # Create the order
        order = Order(user_id=user_id, total_amount=total_amount)
        db.add(order)
        db.commit()  

        # Create order items
        for item in cart_items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=product.price
            )
            db.add(order_item)

        db.query(Cart).filter(Cart.user_id == user_id).delete()
        db.commit()

    return {"message": "Order successfully created", "order_id": order.id}
