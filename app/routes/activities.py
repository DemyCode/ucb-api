from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_session
from app.models import Activity

router = APIRouter(
    prefix="/activities",
    tags=["activities"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_activities(
    session: AsyncSession = Depends(get_session),
):
    return await session.execute(select(Activity))


# @router.post("/")
# async def create_activity(activity: Activity, session=Depends(get_session), response_model=Activity):
#     session.add(activity)
#     session.commit()
#     session.refresh(activity)
#     return activity


# @router.get("/{activity_id}")
# async def read_activity(activity_id: int, session=Depends(get_session), response_model=Activity):
#     activity = session.get(Activity, activity_id)
#     if not activity:
#         raise HTTPException(status_code=404, detail="Activity not found")
#     return activity
