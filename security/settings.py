from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    # App related settings
    APP_NAME: str = "IntelliSense IOT"
    APP_DESCRIPTION: str = "Description"
    API_VERSION: str = "v1"

    # Security related settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database related settings
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_POOL_RECYCLE: int = 900

    class Config:
        env_file = ".env"


settings = Settings()
