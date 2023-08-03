from datetime import timedelta
from typing import Annotated

from auth.Dependency import get_current_user
from auth.utils.tokens import authenticate_user, create_access_token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from project_site.auth.schemas.User import Setting, Token

router = APIRouter(tags=["Auth"])
setting = Setting()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    """this function creates token for authentication."""
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/")
async def read_me(current_user=Depends(get_current_user)):
    print("hellllo--------------------------------")
    """This function shows all the information of logged user.
    This is created for test case"""
    return current_user
