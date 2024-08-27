import enum
from sqlalchemy import Column, ForeignKey, SmallInteger, String, Uuid, Enum
from sqlalchemy.orm import relationship
from database import Base
from .base_entity import BaseEntity


class TaskMode(enum.Enum):
    DONE = 'D'
    INPROGRESS = 'I'
    NEW = 'N'


class Task(BaseEntity, Base):
    __tablename__ = "tasks"

    title = Column(String)
    description = Column(String)
    status = Column(Enum(TaskMode), nullable=False, default=TaskMode.NEW)
    company_id = Column(Uuid, ForeignKey("company.id"), nullable=False)
    owner_id = Column(Uuid, ForeignKey("users.id"), nullable=True)

    company = relationship("Company")
    owner = relationship("User")
