from pydantic import BaseModel
from typing import Optional
from .recipes import Recipe

class MenuItemBase(BaseModel):
    item_name: Optional[str] = None
    price: float
    category: str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int
    recipe: Optional[Recipe] = None  # Relationship with Recipe

    class ConfigDict:
        from_attributes = True