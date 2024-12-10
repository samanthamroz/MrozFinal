from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PromoCodeBase(BaseModel):
    code: str
    percent_off: float
    expiry_date: datetime
    payment_id: int


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    code: Optional[str] = None
    percent_off: Optional[float] = None
    expiry_date: Optional[datetime] = None
    payment_id: Optional[int] = None


class PromoCode(PromoCodeBase):
    id: int

    class ConfigDict:
        from_attributes = True