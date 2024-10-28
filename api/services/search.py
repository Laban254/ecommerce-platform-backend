# api/services/search.py

from sqlalchemy.orm import Session
from api.models.product import Product

class SearchService:
    def __init__(self, db: Session):
        self.db = db

    def search_products(self, name: str = None, category: str = None, min_price: float = None, max_price: float = None):
        query = self.db.query(Product)

        if name:
            query = query.filter(Product.name.ilike(f"%{name}%"))
        
        if category:
            query = query.filter(Product.category == category)
        
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        return query.all()
