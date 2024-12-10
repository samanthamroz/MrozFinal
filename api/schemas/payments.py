from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from api.schemas.customers import Customer
from api.schemas.promo_codes import PromoCode

class PaymentBase(BaseModel):
    card_number: int
    exp_month: int
    exp_year: int
    security_code: int
    name_on_card: str
    paying_customer_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_number: Optional[int] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    security_code: Optional[int] = None
    name_on_card: Optional[str] = None
    paying_customer_id: Optional[int] = None


class Payment(PaymentBase):
    id: int
    promo_code: Optional[PromoCode] = None  # Relationship with PromoCode

    class ConfigDict:
        from_attributes = True