create models/menu_items.py -

from sqlalchemy import Column, Integer, String, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    tablename = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer)
    food_category = Column(String(50))
    ingredients = Column(Text)

    order_details = relationship("OrderDetail", back_populates="menu_item")
    recipe_requirements = relationship("RecipeRequirement", back_populates="menu_item")