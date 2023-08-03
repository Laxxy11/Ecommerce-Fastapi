from datetime import datetime, timedelta

import edgedb
from auth.queries import auth_user_async_edgeql
from auth.utils.hashing import verify_password
from jose import jwt

from project_site.auth.schemas.User import Setting

setting = Setting()
client = edgedb.create_async_client()


async def authenticate_user(username: str, password: str):
    """ "this function authenticate the users by comparing database value
    and the OAuth2PasswordRequestForm values"""
    user = await auth_user_async_edgeql.auth_user(client, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """ "to create jwt token for name"""

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt
