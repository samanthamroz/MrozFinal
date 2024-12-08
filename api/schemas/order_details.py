from pydantic import BaseModel
from typing import Optional
from api.schemas.menu_items import MenuItem


class OrderDetailBase(BaseModel):
    menu_item: MenuItem = None
    amount: int


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(BaseModel):
    menu_item: Optional[MenuItem] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True