# api/routes/notifications.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.services.notifications import NotificationService

notifications = APIRouter()

@notifications.post("/send-email-confirmation/{order_id}")
def send_email_confirmation(order_id: int, email: str, db: Session = Depends(get_db)):
    service = NotificationService(db)
    service.send_email_confirmation(email, order_id)
    return {"message": "Email confirmation sent."}

# @notifications.post("/send-sms-update/{order_id}")
# def send_sms_update(order_id: int, phone_number: str, status: str, db: Session = Depends(get_db)):
#     service = NotificationService(db)
#     service.send_sms_update(phone_number, order_id, status)
#     return {"message": "SMS update sent."}
