import edgedb
from fastapi import APIRouter, status
from user.schemas import user_schema
from utils.response import success_response

from project_site.user.user_views import (
    db_create_users,
    db_get_users,
    db_get_users_by_name,
)

router = APIRouter(tags=["User"])
client = edgedb.create_async_client()


@router.get("/users/", status_code=status.HTTP_200_OK)
async def get_users():
    """Api endpoint for reading all the users"""
    data = await db_get_users(client)
    return await success_response(
        status_code=200,
        msg="Successfully",
        data_info=data,
    )


@router.get("/users/{name}", status_code=status.HTTP_200_OK)
async def get_user_by_name(name: str):
    """Api Endpoint for reading user by name"""
    data = await db_get_users_by_name(client, name)
    return await success_response(
        status_code=200,
        msg="Successfully ",
        data_info=data,
    )


@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: user_schema.UserCreate):
    """Api Endpoint for creating new user"""
    data = await db_create_users(client, user)
    return await success_response(
        status_code=200,
        msg="Successfully",
        data_info=data,
    )
