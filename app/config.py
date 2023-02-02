from typing import List

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str = "ucb-api"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: PostgresDsn = PostgresDsn("postgresql+asyncpg://postgres:postgres@db:5432/postgres")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    UPDATE_ALEMBIC: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        env_nested_delimiter = "__"


settings = Settings()
