from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Review(Base):
    """
    rating : int
    review : string
    """
    __tablename__ = "customers"

    rating = Column(Integer, nullable=False)
    review = Column(String, nullable=False)