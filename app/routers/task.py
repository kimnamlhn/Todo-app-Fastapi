from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from uuid import UUID

from schemas.user import User
from services.exception import AccessDeniedError, ResourceNotFoundError
from database import get_db_context
from schemas.task import Task
from models.task import TaskModel, TaskViewModel
from services import auth as AuthService
from services import task as TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[TaskViewModel])
async def get_tasks(db: Session = Depends(get_db_context)) -> List[TaskViewModel]:
    return db.query(Task).all()

@router.get("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskViewModel)
async def get_task_by_id(
    task_id: UUID,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)): 
      
    if not user.is_admin:
        raise AccessDeniedError()
    
    task = TaskService.get_task_by_id(db, task_id)

    if task is None:
        raise ResourceNotFoundError()

    return task


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskViewModel)
async def create_task(
    request: TaskModel,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)): 
    
    if not user.is_admin:
        raise AccessDeniedError()
    
    return TaskService.add_new_task(db, request)


@router.put("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskViewModel)
async def update_task(
    task_id: UUID,
    request: TaskModel,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)): 

    
    if not user.is_admin:
        raise AccessDeniedError()
    
    return TaskService.update_task(db, task_id, request)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)): 
    
    if not user.is_admin:
        raise AccessDeniedError()
    
    TaskService.delete_task(db, task_id)