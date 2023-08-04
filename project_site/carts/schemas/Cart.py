from uuid import UUID

from pydantic import BaseModel


class CartBase(BaseModel):
    quantity: int
    user_id: UUID
    product_id: UUID


class CartCreate(BaseModel):
    quantity: int
    product: str
