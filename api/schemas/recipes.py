from pydantic import BaseModel
from typing import Optional
from api.schemas.resources import Resource


class RecipeBase(BaseModel):
    item_name: str
    resource_name: str
    amount: int


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    item_name: Optional[str] = None
    resource_name: Optional[str] = None
    amount: Optional[int] = None


class Recipe(RecipeBase):
    id: int
    resource: Optional[Resource] = None  # Relationship with Resource

    class ConfigDict:
        from_attributes = True