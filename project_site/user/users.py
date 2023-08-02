from fastapi import APIRouter,HTTPException,Depends,status
import edgedb
from typing import List
router=APIRouter(
    
    tags=['User']
)

@router.get("/users/",status_code=status.HTTP_200_OK,response_model=List[User])
async def get_users():
    users=await get_user_async_edgeql.get_user(client)
    print(users)
    return users

@router.get("/users/{name}",status_code=status.HTTP_200_OK,response_model=User)
async def get_user_by_name(name:str):
    db_user=await get_user_by_name_async_edgeql.get_user_by_name(client,username=name)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Username '{name}' does not exist."},
        )
    return db_user