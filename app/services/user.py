from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.task import Task
from services import utils
from models.user import SearchUserModel, UserModel, UserViewModel
from schemas.user import User, get_password_hash
from services.exception import InvalidInputError, ResourceNotFoundError
from services import company as CompanyService

def get_all_users(db: Session, conds: SearchUserModel) -> List[User]:
    query = select(User).options(
        joinedload(User.company, innerjoin=True))
    
    if conds.email is not None:
        query = query.filter(User.email.like(f"%{conds.email}%"))
    if conds.company_id is not None:
        query = query.filter(User.company_id == conds.company_id)
    
    query = query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()

def get_user_by_id(db: Session, user_id: UUID) -> User:
    return db.scalars(select(User).filter(User.id == user_id)).first()

def is_email_exist(db: Session, email: str) -> User:
    user =  db.scalars(select(User).filter(User.email == email)).first()
       
    return user is not None

def is_username_exist(db: Session, username: UUID) -> User:
    user =  db.scalars(select(User).filter(User.username == username)).first()
       
    return user is not None

def get_user_by_id(db: Session, user_id: UUID) -> User:
    return db.scalars(select(User).filter(User.id == user_id)).first()

def add_new_user(db: Session, data: UserModel) -> User:
    company = CompanyService.get_company_by_id(db, data.company_id)
        
    if company is None:
        raise InvalidInputError("Invalid company information")
    
    isEmailExist = is_email_exist(db, data.email)
    
    if isEmailExist is True:
        raise InvalidInputError("Email already exists.")

    isUsernameExist = is_username_exist(db, data.username)
    
    if isUsernameExist is True:
        raise InvalidInputError("Username already exists.")
    
    user = User(**data.model_dump())

    user.created_at = utils.get_current_utc_time()
    user.updated_at = utils.get_current_utc_time()
    user.password = get_password_hash(user.password)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def update_user(db: Session, id: UUID, data: UserModel) -> User:
    user = get_user_by_id(db, id)

    if user is None:
        raise ResourceNotFoundError()

    company = CompanyService.get_company_by_id(db, data.company_id)
        
    if company is None:
        raise InvalidInputError("Invalid company information")

    isEmailExist = is_email_exist(db, data.email)
    
    if isEmailExist is True:
        raise InvalidInputError("Email already exists.")

    isUsernameExist = is_username_exist(db, data.username)
    
    if isUsernameExist is True:
        raise InvalidInputError("Username already exists.")
    
    user.email = data.email
    user.username = data.username
    user.password = get_password_hash(data.password) 
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.is_active = data.is_active
    user.is_admin = data.is_admin
    user.company_id = data.company_id

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, id: UUID) -> None:
    user = get_user_by_id(db, id)

    if user is None:
        raise ResourceNotFoundError()

    isUserHaveAnyTasks = is_user_have_any_tasks(db, id)
    
    if isUserHaveAnyTasks is True:
        raise InvalidInputError("Please delete all tasks belonging to this user before deletion")  
    
    db.delete(user)
    db.commit()

def is_user_have_any_tasks(db: Session, user_id: UUID) -> None:
    user =  db.scalars(select(Task).filter(Task.owner_id == user_id)).first()
       
    return user is not None