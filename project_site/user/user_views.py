from auth.utils.hashing import get_password_hash
from fastapi import HTTPException, status

from .queries import (
    create_user_async_edgeql,
    get_user_async_edgeql,
    get_user_by_name_async_edgeql,
)


async def db_get_users(client):
    users = await get_user_async_edgeql.get_user(client)
    return users


async def db_get_users_by_name(client, name):
    db_user = await get_user_by_name_async_edgeql.get_user_by_name(
        client, username=name
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Username '{name}' does not exist."},
        )
    return db_user


async def db_create_users(client, user):
    db_user = await get_user_by_name_async_edgeql.get_user_by_name(
        client,
        username=user.username,
    )
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist",
        )
    hash_password = get_password_hash(user.password)
    db_user = await create_user_async_edgeql.create_user(
        client,
        username=user.username,
        email=user.email,
        password=hash_password,
        user_role=user.user_role,
    )
    return db_user
