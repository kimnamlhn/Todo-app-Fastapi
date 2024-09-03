from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from database import get_db_context
from schemas.task import Task
from models.task import TaskViewModel

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[TaskViewModel])
async def get_tasks(db: Session = Depends(get_db_context)) -> List[TaskViewModel]:
    return db.query(Task).all()
