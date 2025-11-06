create schemas/menu_items.py -

from typing import Optional
from pydantic import BaseModel
from decimal import Decimal

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    calories: Optional[int] = None
    food_category: Optional[str] = None
    ingredients: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None
    ingredients: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True