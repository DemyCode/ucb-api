import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger
from sqlmodel import Session

import alembic.command
import alembic.config
from app.config import settings
from app.db import engine
from app.models import User
from app.routes import activities

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

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
    async def alembic_upgrade():
        logger.info("Attempting to upgrade alembic on startup")
        alembic_cfg = alembic.config.Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))
        alembic.command.upgrade(alembic_cfg, "head")
        logger.info("Successfully upgraded alembic on startup")


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     with Session(engine) as session:
#         user = session.get(User, form_data.username)
#         if not user:
#             raise HTTPException(status_code=400, detail="Incorrect username or password")
#         return {"access_token": user.username, "token_type": "bearer"}


app.include_router(activities.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
