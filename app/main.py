from typing import Optional
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, SQLModel, create_engine


from app.models import User
from app.db import get_session, init_db
from app.config import get_settings

settings = get_settings()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router()


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
