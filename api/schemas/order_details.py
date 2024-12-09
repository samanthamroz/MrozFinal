from pydantic import BaseModel
from typing import Optional
from api.schemas.menu_items import MenuItem


class OrderDetailBase(BaseModel):
    menu_item: MenuItem = None
    order_id: int = None
    amount: int = None


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(BaseModel):
    menu_item: Optional[MenuItem] = None
    amount: Optional[int] = None
    order_id: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True