from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .customers import Customer
from .order_details import OrderDetail


class OrderBase(BaseModel):
    date: datetime
    status: bool
    price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    date: Optional[datetime] = None
    status: Optional[bool] = None
    price: Optional[float] = None


class Order(OrderBase):
    id: int
    customer: Customer = None  # Relationship with Customer
    order_details: OrderDetail = None  # Relationship with OrderDetail

    class Config:
        from_attributes = True