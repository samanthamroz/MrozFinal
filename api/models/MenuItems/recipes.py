from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    item_name = Column(Integer, ForeignKey("menu_items.item_name"))
    resource_name = Column(Integer, ForeignKey("resources.resource_name"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    menu_item = relationship("MenuItems", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")