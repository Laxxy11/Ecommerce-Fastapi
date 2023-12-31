# AUTOGENERATED FROM 'project_site/user/queries/delete_user.edgeql' WITH:
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
class DeleteUserResult(NoPydanticValidation):
    id: uuid.UUID
    username: str
    email: str
    user_role: str


async def delete_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    username: str,
) -> DeleteUserResult | None:
    return await executor.query_single(
        """\
        select (
            delete User filter(User.username=<str>$username)
        )
        {
            username,email,user_role,
        }\
        """,
        username=username,
    )
