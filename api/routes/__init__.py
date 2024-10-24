from fastapi import APIRouter
from .auth import auth


api_version_one = APIRouter(prefix="/api/v1")


api_version_one.include_router(auth)
