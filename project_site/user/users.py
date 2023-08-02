from fastapi import APIRouter,HTTPException,Depends,status
import edgedb
from typing import List
from schemas import user_schema 
from .queries import create_user_async_edgeql,get_user_async_edgeql,get_user_by_name_async_edgeql



router=APIRouter(
    
    tags=['User']
)
client = edgedb.create_async_client()

@router.get("/users/",status_code=status.HTTP_200_OK,response_model=List[user_schema.User])
async def get_users():
    """Api endpoint for reading all the users"""
    users=await get_user_async_edgeql.get_user(client)
    print(users)
    return users

@router.get("/users/{name}",status_code=status.HTTP_200_OK,response_model=user_schema.User)
async def get_user_by_name(name:str):
    """Api Endpoint for reading user by name"""
    db_user=await get_user_by_name_async_edgeql.get_user_by_name(client,username=name)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Username '{name}' does not exist."},
        )
    return db_user

@router.post("/users/",status_code=status.HTTP_201_CREATED,response_model=user_schema.User)
async def create_user(user:user_schema.UserCreate):
    """Api Endpoint for creating new user"""
    db_user=await get_user_by_name_async_edgeql.get_user_by_name(client,username=user.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exist")
    db_user=await create_user_async_edgeql.create_user(client,username=user.username,email=user.email,password=user.password)
    return db_user