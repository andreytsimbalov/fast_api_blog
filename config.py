import os
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

    @property
    def __database_url_postfix(self):
        # postgres:postgres@localhost:5432/db_name
        return f"{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def database_url_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/db_name
        return f"postgresql+asyncpg://{self.__database_url_postfix}"

    @property
    def database_url_psycopg(self):
        # postgresql+psycopg://postgres:postgres@localhost:5432/db_name
        return f"postgresql+psycopg://{self.__database_url_postfix}"

    model_config = SettingsConfigDict(env_file=f"{os.path.dirname(__file__)}/.env")


settings = Settings()
