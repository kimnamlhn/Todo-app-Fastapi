import uuid
from database import Base
from sqlalchemy import Column, String, Uuid, Enum
from sqlalchemy.orm import relationship
from .base_entity import BaseEntity, Gender

class Company(Base, BaseEntity):
    __tablename__ = "company"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    company_name = Column(String)
    address = Column(Enum(Gender), nullable=False, default=Gender.NONE)

    books = relationship("Book", back_populates="author")
