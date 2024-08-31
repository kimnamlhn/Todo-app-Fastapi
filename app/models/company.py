from pydantic import BaseModel, Field
from schemas.base_entity import Gender
from datetime import datetime
from uuid import UUID

class CompanyModel(BaseModel):
    full_name: str = Field(min_length=2)


class CompanyViewModel(BaseModel):
    id: UUID 
    name: str
    description: str
    mode: str
    rating: int
    
    class Config:
        from_attributes = True