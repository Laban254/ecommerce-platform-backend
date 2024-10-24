# routes/product.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from api.services.product import ProductService
from api.models.user import User
from api.services.user import user_service
from api.utils.success_response import auth_response, success_response

product_router = APIRouter(prefix="/products", tags=["Product Management"])


@product_router.post("/",  status_code=status.HTTP_201_CREATED)
async def create_product(
    schema: ProductCreate,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_admin),
):
    product = ProductService.create_product(db=db, product=schema)

    return {
        "status_code": status.HTTP_201_CREATED,
        "message": "Product created successfully",
        "product": product
    }

@product_router.put("/{id}",  status_code=status.HTTP_200_OK)
async def update_product(
    id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(user_service.get_current_admin),
):
    updated_product = ProductService.update_product(db=db, product_id=id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Product updated successfully",
        "product": updated_product
    }

@product_router.delete("/{id}",  status_code=status.HTTP_200_OK)
async def delete_product(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(user_service.get_current_admin),
):
    deleted_product = ProductService.delete_product(db=db, product_id=id)
    if deleted_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Product deleted successfully",
        "product": deleted_product
    }

@product_router.get("/",  status_code=status.HTTP_200_OK)
async def get_products(db: Session = Depends(get_db)):
    products = ProductService.get_products(db=db)
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Products retrieved successfully",
        "products": products
    }

@product_router.get("/{id}",  status_code=status.HTTP_200_OK)
async def get_product(
    id: int,
    db: Session = Depends(get_db),
):
    product = ProductService.get_product(db=db, product_id=id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Product retrieved successfully",
        "product": product
    }