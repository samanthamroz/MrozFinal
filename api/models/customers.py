from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(13), nullable=False)
    address = Column(String(100), nullable=False)

    payment = relationship("Payment", back_populates="customer")

    reviews = relationship("Review", back_populates="customer")

    orders = relationship("Order", back_populates="customer")