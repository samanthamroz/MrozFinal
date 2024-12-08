from pydantic import BaseModel
from typing import Optional


class ResourceBase(BaseModel):
    resource_name: str
    amount_in_inventory: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    resource_name: Optional[str] = None
    amount_in_inventory: Optional[int] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True