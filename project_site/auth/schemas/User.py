from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str | None = None


# for loading a settings or config class from environment variables or secrets files.
class Setting(BaseSettings):
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
