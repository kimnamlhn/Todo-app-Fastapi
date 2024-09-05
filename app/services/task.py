from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from services import utils
from models.task import SearchTaskModel, TaskModel, TaskViewModel
from schemas.task import Task
from services.exception import InvalidInputError, ResourceNotFoundError
from services import user as UserService

def get_all_tasks(db: Session, conds: SearchTaskModel) -> List[Task]:
    query = select(Task).options(
        joinedload(Task.owner, innerjoin=True))
    
    if conds.summary is not None:
        query = query.filter(Task.summary.like(f"%{conds.summary}%"))
    if conds.owner_id is not None:
        query = query.filter(Task.owner_id == conds.owner_id)
    
    query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()

def get_task_by_id(db: Session, task_id: UUID) -> Task:
    return db.scalars(select(Task).filter(Task.id == task_id)).first()

def add_new_task(db: Session, data: TaskModel) -> Task:
    owner = UserService.get_user_by_id(db, data.owner_id)
        
    if owner is None:
        raise InvalidInputError("Invalid owner information")
    
    task = Task(**data.model_dump())

    task.created_at = utils.get_current_utc_time()
    task.updated_at = utils.get_current_utc_time()
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def update_task(db: Session, id: UUID, data: TaskModel) -> Task:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()
    
    owner = UserService.get_user_by_id(db, data.owner_id)
        
    if owner is None:
        raise InvalidInputError("Invalid owner information")
    
    task.summary = data.summary
    task.description = data.description
    task.status = data.status
    task.priority = data.priority
    task.owner_id = data.owner_id

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, id: UUID) -> None:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()
    
    db.delete(task)
    db.commit()
