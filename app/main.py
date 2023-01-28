from typing import Optional
import uvicorn
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, SQLModel, create_engine
from loguru import logger
import alembic.command
import alembic.config

from app.models import User
from app.db import get_session, init_db
from app.config import settings

settings = settings()

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if settings.UPDATE_ALEMBIC:

    @app.on_event("startup")
    def alembic_upgrade():
        logger.info("Attempting to upgrade alembic on startup")
        try:
            alembic_ini_path = Path(__file__).parent / "alembic.ini"
            alembic_cfg = alembic.config.Config(str(alembic_ini_path))
            alembic_cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URI)
            alembic.command.upgrade(alembic_cfg, "head")
            logger.info("Successfully upgraded alembic on startup")
        except Exception:
            logger.exception("Alembic upgrade failed on startup")


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.get(User, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def fake_hash_password(password: str):
        return "fakehashed" + password

    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
