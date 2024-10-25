from fastapi import APIRouter
from .auth import auth
from .product import product_router
from .cart import cart
from .checkout import checkout_t
from .order import order_router 

api_version_one = APIRouter(prefix="/api/v1")


api_version_one.include_router(auth)
api_version_one.include_router(product_router)
api_version_one.include_router(cart)
api_version_one.include_router(checkout_t)
api_version_one.include_router(order_router )