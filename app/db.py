from sqlmodel import create_engine, SQLModel, Session
from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
