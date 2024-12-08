from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, primary_key=True, nullable=False)
    percent_off = Column(DECIMAL, nullable=False)
    expiry_date = Column(DATETIME, nullable=False)