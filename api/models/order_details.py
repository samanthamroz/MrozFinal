from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details.py"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Integer, index=True, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="order_details")

    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    menu_item = relationship("MenuItem", back_populates="order_details")