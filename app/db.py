from sqlmodel import create_engine
from app.config import settings
from sqlmodel import Session

engine = create_engine(settings.DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
