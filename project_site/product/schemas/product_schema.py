from typing import List

from pydantic import BaseModel


# this pydantic model for category
class Category(BaseModel):
    category: str


# this pydantic model for Product base
class Product(BaseModel):
    title: str
    description: str
    price: float
    categories: List[str]
