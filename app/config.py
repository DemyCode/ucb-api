from typing import List, Optional

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
)


class Settings(BaseSettings):
    PROJECT_NAME: str = "ucb-api"
    API_V1_STR: str = "/api/v1"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    DATABASE_URI: Optional[PostgresDsn] = None
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    UPDATE_ALEMBIC: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        env_nested_delimiter = "__"


settings = Settings()
