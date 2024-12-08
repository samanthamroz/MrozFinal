from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Review(Base):
    """
    rating : int
    review : string
    """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(Integer, ForeignKey("menu_items.item_name"))
    rating = Column(Integer, nullable=False)
    review = Column(String(100), nullable=False)
    customer = relationship("Customer", back_populates="reviews")