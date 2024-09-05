from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_admin: bool

class UserCreate(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_admin: bool
    company_id: UUID
    
class UserBaseModel(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    first_name: str
    last_name: str
    
    class Config:
        from_attributes = True

class UserViewModel(UserBaseModel):
    is_admin: bool
    is_active: bool
    company_id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None
