# AUTOGENERATED FROM 'project_site/auth/queries/auth_user.edgeql' WITH:
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
class AuthUserResult(NoPydanticValidation):
    id: uuid.UUID
    username: str
    password: str
    email: str


async def auth_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    username: str,
) -> AuthUserResult | None:
    return await executor.query_single(
        """\
        select User {username,password,email}filter(User.username=<str>$username)\
        """,
        username=username,
    )
