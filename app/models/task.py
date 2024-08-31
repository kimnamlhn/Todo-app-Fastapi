from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

from models.company import CompanyViewModel
from models.user import UserBaseModel
from schemas.task import TaskMode


class SearchTaskModel():
    def __init__(self, title, author_id, page, size) -> None:
        self.title = title
        self.author_id = author_id
        self.page = page
        self.size = size

class TaskModel(BaseModel):
    title: str
    description: Optional[str]
    author_id: UUID
    status: TaskMode = Field(default=TaskMode.DRAFT)
    owner_id: Optional[UUID] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Task 1",
                "description": "Description for Task 1",
                "author_id": "123e4567-e89b-12d3-a456-426614174000",
                "status": "NEW"
            }
        }

class TaskViewModel(BaseModel):
    id: UUID
    title: str
    summary: str | None = None
    description: str | None = None
    status: TaskMode = Field(default=TaskMode.NEW)
    priority: int
    owner_id: UUID | None = None
    owner: UserBaseModel | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True