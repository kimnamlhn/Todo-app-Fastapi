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
    summary = Column(String)
    description = Column(String)
    status = Column(Enum(TaskMode), nullable=False, default=TaskMode.NEW)
    priority = Column(SmallInteger)
    owner_id = Column(Uuid, ForeignKey("users.id"), nullable=True)

    owner = relationship("User")