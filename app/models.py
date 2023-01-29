from __future__ import annotations

from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class UserActivityLink(SQLModel, table=True):
    activity_id: Optional[int] = Field(default=None, foreign_key="activity.id", primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    grade: Optional[float] = Field(default=None)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    activities: List[Activity] = Relationship(back_populates="users", link_model=UserActivityLink)


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    users: List[User] = Relationship(back_populates="teams", link_model=UserActivityLink)
