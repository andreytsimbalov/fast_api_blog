import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App settings
    debug: bool = False
    host: str = 'localhost'
    port: int = 8000
    workers: int = 1
    timeout: float = 0.5
    max_timeout_count: int = 10

    # DataBase settings
    db_name: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: str

    model_config = SettingsConfigDict(env_file=f"{os.path.dirname(__file__)}/.env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
