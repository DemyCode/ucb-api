from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "UCB API"

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
