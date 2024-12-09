from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    item_name = Column(String(100), unique=True, nullable=False)

    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    menu_item = relationship("MenuItem", back_populates="recipe")

    resource_name = Column(Integer, ForeignKey("resources.resource_name"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')
    resource = relationship("Resource", back_populates="recipes")