from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models import Activity
from app.db import get_session

router = APIRouter(
    prefix="/activities",
    tags=["activities"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_session)],
)


@router.get("/")
async def read_activities(response_model=List[Activity], session=Depends(get_session)):
    return session.exec(Activity.select()).all()


@router.post("/")
async def create_activity(
    activity: Activity, session=Depends(get_session), response_model=Activity
):
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity


@router.get("/{activity_id}")
async def read_activity(
    activity_id: int, session=Depends(get_session), response_model=Activity
):
    activity = session.get(Activity, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity
