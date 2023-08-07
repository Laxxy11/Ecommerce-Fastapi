import edgedb
from auth.Dependency import get_current_user
from fastapi import APIRouter, Depends, status
from user.route.user_views import db_create_users, db_get_users, db_get_users_by_name
from user.schemas import user_schema
from utils.response import success_response

router = APIRouter(tags=["User"])
client = edgedb.create_async_client()


@router.get("/users/", status_code=status.HTTP_200_OK)
async def get_users(user=Depends(get_current_user)):
    """Api endpoint for reading all the users"""
    data = await db_get_users(client, user_id=user.id)
    return await success_response(
        status_code=200,
        msg="Successfully",
        data_info=data,
    )


@router.get("/user/get/{user_name}", status_code=status.HTTP_200_OK)
async def get_user_by_name(name: str):
    """Api Endpoint for reading user by name"""
    data = await db_get_users_by_name(client, name)
    return await success_response(
        status_code=200,
        msg="Successfully ",
        data_info=data,
    )


@router.post("/user/create/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: user_schema.UserCreate, current_user=Depends(get_current_user)
):
    """Api Endpoint for creating new user"""
    data = await db_create_users(client, user, admin_id=current_user.id)
    return await success_response(
        status_code=200,
        msg="Successfully",
        data_info=data,
    )
