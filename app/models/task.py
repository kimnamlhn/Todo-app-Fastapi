from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

from models.user import UserViewModel
from schemas.task import TaskMode

class SearchTaskModel():
    def __init__(self, summary, owner_id, page, size) -> None:
        self.summary = summary
        self.owner_id = owner_id
        self.page = page
        self.size = size
        
class TaskModel(BaseModel):
    summary: str | None = None
    description: str | None = None
    status: TaskMode = Field(default=TaskMode.NEW)
    priority: int | None = None
    owner_id: UUID | None = None

class TaskViewModel(BaseModel):
    id: UUID
    summary: str | None = None
    description: str | None = None
    status: TaskMode = Field(default=TaskMode.NEW)
    priority: int
    owner_id: UUID | None = None
    owner: UserViewModel | None = None  
    
    class Config:
        from_attributes = True
              