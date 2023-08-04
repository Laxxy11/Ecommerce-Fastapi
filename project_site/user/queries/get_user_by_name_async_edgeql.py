# AUTOGENERATED FROM 'project_site/user/queries/get_user_by_name.edgeql' WITH:
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
class GetUserByNameResult(NoPydanticValidation):
    id: uuid.UUID
    username: str
    email: str
    user_role: str


async def get_user_by_name(
    executor: edgedb.AsyncIOExecutor,
    *,
    username: str,
) -> GetUserByNameResult | None:
    return await executor.query_single(
        """\
        select User {username,email,user_role}filter(User.username=<str>$username)\
        """,
        username=username,
    )
