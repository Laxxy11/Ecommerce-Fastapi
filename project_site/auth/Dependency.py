from typing import Annotated

import edgedb
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from user.views import db_get_users_by_name

from project_site.auth.schemas.User import Setting, TokenData

setting = Setting()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
client = edgedb.create_async_client()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """to get user information from payload of jwt and in this case username"""

    print("-----------------------------------------------------------------------")

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentails",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(name=username)
    except JWTError:
        raise credentials_exception
    print("---------------------------------------------------------")
    print(token_data.name)
    user = await db_get_users_by_name(client, name=token_data.name)
    # user = await auth_user_async_edgeql.auth_user(client, username=token_data.name)
    if user is None:
        raise credentials_exception
    return user
