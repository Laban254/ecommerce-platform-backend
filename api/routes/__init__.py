from fastapi import APIRouter
from .auth import auth
from .product import product_router

api_version_one = APIRouter(prefix="/api/v1")


api_version_one.include_router(auth)
api_version_one.include_router(product_router)
