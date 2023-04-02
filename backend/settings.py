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

    # AWS related settings (only for reference)
    AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_REGION: str = os.getenv('AWS_DEFAULT_REGION')
    AWS_IOT_ENDPOINT: str = os.getenv('AWS_IOT_ENDPOINT')
    AWS_KINESIS_STREAM_NAME: str = os.getenv('AWS_KINESIS_STREAM_NAME')
    AWS_IOT_THING_NAME: str = os.getenv('AWS_IOT_THING_NAME')

    class Config:
        env_file = ".env"


settings = Settings()
