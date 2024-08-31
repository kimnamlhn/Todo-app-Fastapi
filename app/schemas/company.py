import uuid
from database import Base
from sqlalchemy import Column, SmallInteger, String, Uuid
from .base_entity import BaseEntity

class Company(Base, BaseEntity):
    __tablename__ = "company"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String)
    mode = Column(String)
    rating = Column(SmallInteger)