from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import datetime


class PromoCodeBase(BaseModel):
    code: str
    percent_off: float
    expiry_date: datetime


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    code: Optional[str] = None
    percent_off: Optional[float] = None
    expiry_date: Optional[datetime] = None


class PromoCode(PromoCodeBase):
    id: int

    class ConfigDict:
        from_attributes = True