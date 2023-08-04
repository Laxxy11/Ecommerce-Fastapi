from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    user_role: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_role: str = "user"
