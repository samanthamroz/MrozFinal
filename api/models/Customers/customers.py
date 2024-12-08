from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Customer(Base):
    """
    name : String
    email : String
    phone : int
    address : String
    payment : Payment
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    payment = relationship("Payment", back_populates="customer")
