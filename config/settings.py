from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_ENV: str = "develop"
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USERNAME: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
