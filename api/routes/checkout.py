from api.services.checkout import process_checkout
from api.schemas.order import OrderResponse
from fastapi import HTTPException, status
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.models.user import User
from api.services.user import user_service

checkout_t = APIRouter()


@checkout_t.post("/checkout", response_model=OrderResponse)
async def checkout(user: User = Depends(user_service.get_current_user), db: Session = Depends(get_db)):
    """
    Process the checkout for the authenticated user.
    This endpoint processes the user's cart and creates an order.
    """
    try:
        result = process_checkout(user_id=user.id, db=db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
