""" User data model
"""

from sqlalchemy import Column, String, text, Boolean
from sqlalchemy.orm import relationship
# from api.models.associations import user_organisation_association
# from api.models.permissions.user_org_role import user_organisation_roles
from api.models.base_model import BaseTableModel


class User(BaseTableModel):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    is_active = Column(Boolean, server_default=text("true"))
    role = Column(String, nullable=False, server_default=text("'user'"))
    is_deleted = Column(Boolean, server_default=text("false"))
    is_verified = Column(Boolean, server_default=text("false"))
    
    cart_items = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")
    wishlists = relationship("Wishlist", back_populates="user")


    token_login = relationship(
         "TokenLogin", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )

    def to_dict(self):
        obj_dict = super().to_dict()
        obj_dict.pop("password")
        return obj_dict

    def __str__(self):
        return self.email