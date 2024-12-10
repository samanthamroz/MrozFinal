from pydantic import BaseModel
from typing import Optional
from api.schemas.customers import Customer

class ReviewBase(BaseModel):
    item_name: Optional[str] = None
    rating: int
    review: str
    customer_id: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    item_name: Optional[str] = None
    rating: Optional[int] = None
    review: Optional[str] = None
    customer_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    customer: Customer = None  # Relationship with Customer

    class ConfigDict:
        from_attributes = True