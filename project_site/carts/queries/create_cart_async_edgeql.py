# AUTOGENERATED FROM 'project_site/carts/queries/create_cart.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations

import dataclasses
import uuid

import edgedb


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass

        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class CreateCartResult(NoPydanticValidation):
    id: uuid.UUID
    user: CreateCartResultUser
    products: list[CreateCartResultProductsItem]
    quantity: int


@dataclasses.dataclass
class CreateCartResultProductsItem(NoPydanticValidation):
    id: uuid.UUID
    title: str


@dataclasses.dataclass
class CreateCartResultUser(NoPydanticValidation):
    id: uuid.UUID
    username: str


async def create_cart(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
    title: str,
    quantity: int,
) -> CreateCartResult:
    return await executor.query_single(
        """\
        select(
            insert Cart{
            user:=(select User filter .id =<uuid>$user_id),
            products := (select Product filter .title =<str>$title ),
            quantity:=<int64>$quantity
        })
        {
            user:{username},products:{title},quantity
        };\
        """,
        user_id=user_id,
        title=title,
        quantity=quantity,
    )
