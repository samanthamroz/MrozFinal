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
    promo_code : Code
    """
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_number = Column(Integer, nullable=False)
    exp_month = Column(Integer, nullable=False)
    exp_year = Column(Integer, nullable=False)
    security_code = Column(Integer, nullable=False)
    name_on_card = Column(String(100), nullable=False)

    promo_code = relationship("PromoCode", back_populates="payments")