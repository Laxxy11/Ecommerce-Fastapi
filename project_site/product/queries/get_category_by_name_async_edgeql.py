# AUTOGENERATED FROM 'project_site/product/queries/get_category_by_name.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetCategoryByNameResult(NoPydanticValidation):
    id: uuid.UUID
    name: str


async def get_category_by_name(
    executor: edgedb.AsyncIOExecutor,
    *,
    name: str,
) -> GetCategoryByNameResult | None:
    return await executor.query_single(
        """\
        select Category {name} filter Category.name=<str>$name\
        """,
        name=name,
    )
