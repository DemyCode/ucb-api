from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "UCB API"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/ucb"


def get_settings():
    return Settings()
