from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    status = Column(Boolean, default=False)
    price = Column(DECIMAL, nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", back_populates="orders")

    order_details = relationship("OrderDetail", back_populates="orders")