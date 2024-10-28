# api/services/notifications.py

import smtplib
from fastapi import HTTPException
from sqlalchemy.orm import Session
# from sms_service import SMSService 
from api.db.database import get_db

class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        # self.sms_service = SMSService()  # Initialize  SMS service 

    def send_email_confirmation(self, email: str, order_id: int):
        try:
            with smtplib.SMTP("smtp.your-email-provider.com", 587) as server:
                server.starttls()
                server.login("your_email@example.com", "your_password")
                subject = "Order Confirmation"
                body = f"Thank you for your order! Your order ID is {order_id}."
                msg = f"Subject: {subject}\n\n{body}"
                server.sendmail("your_email@example.com", email, msg)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # def send_sms_update(self, phone_number: str, order_id: int, status: str):
    #     message = f"Your order ID {order_id} status has been updated to: {status}."
    #     response = self.sms_service.send_sms(phone_number, message)  
    #     if not response.success:  # todo: update to use africas talking
    #         raise HTTPException(status_code=500, detail="Failed to send SMS notification.")
