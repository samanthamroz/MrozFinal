from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_name = Column(String, unique=True, nullable=False)
    amount_in_inventory = Column(Integer, index=True, nullable=False, server_default='0.0')