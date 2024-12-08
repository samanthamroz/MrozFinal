from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Payment(Base):
    """
    card number: int
    exp month : int
    exp year : int
    security code : int
    name : String
    """
    __tablename__ = "customers"

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
