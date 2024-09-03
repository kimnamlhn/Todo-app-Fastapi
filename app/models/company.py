from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class CompanyModel(BaseModel):
    name: str = Field(min_length=2)
    description: str = Field(min_length=2)
    mode: str
    rating: int
    
class CompanyViewModel(BaseModel):
    id: UUID 
    name: str
    description: str
    mode: str
    rating: int
    
    class Config:
        from_attributes = True