# api/routes/search.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.services.search import SearchService
from api.schemas.product import ProductOut
from typing import List, Optional

search = APIRouter()

@search.get("/products/search", response_model=List[ProductOut])
def search_products(
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db)
):
    search_service = SearchService(db)
    products = search_service.search_products(name=name, category=category, min_price=min_price, max_price=max_price)
    return products
