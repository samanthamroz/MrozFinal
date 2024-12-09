from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from api.schemas.customers import Customer
from api.schemas.order_details import OrderDetail


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class OrderDetailCreate(BaseModel):
    menu_item_name: str  # Use the name of the menu item to calculate price
    amount: int  # Quantity of the menu item


class OrderBase(BaseModel):
    date: datetime
    status: bool
    price: float


class OrderCreate(BaseModel):
    date: Optional[datetime] = None
    status: bool
    customer: CustomerCreate
    order_details: List[OrderDetailCreate]


class OrderUpdate(BaseModel):
    date: Optional[datetime] = None
    status: Optional[bool] = None
    price: Optional[float] = None


class Order(OrderBase):
    id: int
    customer: Customer = None  # Relationship with Customer
    order_details: List[OrderDetail] = []  # Relationship with OrderDetail

    class Config:
        from_attributes = True