from pydantic import BaseModel
from typing import Optional
from api.schemas.payment import Payment

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int
    payment: Optional[Payment] = None  # List of Payments

    class ConfigDict:
        from_attributes = True