from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from models.company import CompanyViewModel

class SearchUserModel():
    def __init__(self, email, company_id, page, size) -> None:
        self.email = email
        self.company_id = company_id
        self.page = page
        self.size = size

class UserModel(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_admin: bool
    company_id: UUID | None = None

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
    created_at: datetime | None = None
    updated_at: datetime | None = None
    company_id: UUID | None = None
    company: CompanyViewModel | None = None  
    
