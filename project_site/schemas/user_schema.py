from pydantic import BaseModel,EmailStr
class User(BaseModel):
    username:str
    email:EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    