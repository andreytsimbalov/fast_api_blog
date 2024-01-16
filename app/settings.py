from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    host: str = 'localhost'
    port: int = 8000
    workers: int = 1
    timeout: float = 0.5
    max_timeout_count: int = 10

    db_name: str
    db_user: str
    db_pass: str = None
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file="../.env")


@lru_cache
def get_settings():
    return Settings()
