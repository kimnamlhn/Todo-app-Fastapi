from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class SearchCompanyModel():
    def __init__(self, name, page, size) -> None:
        self.name = name
        self.page = page
        self.size = size

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