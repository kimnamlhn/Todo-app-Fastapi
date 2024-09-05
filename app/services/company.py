from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import User
from services import utils
from models.company import CompanyModel, SearchCompanyModel
from schemas.company import Company
from services.exception import InvalidInputError, ResourceNotFoundError

def get_all_companies(db: Session, conds: SearchCompanyModel) -> List[Company]:
    query = select(Company)
    
    if conds.name is not None:
        query = query.filter(Company.name.like(f"%{conds.name}%"))
    
    query = query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()

def get_company_by_id(db: Session, company_id: UUID) -> Company:
    return db.scalars(select(Company).filter(Company.id == company_id)).first()

def add_new_company(db: Session, data: CompanyModel) -> Company:
    company = Company(**data.model_dump())

    company.created_at = utils.get_current_utc_time()
    company.updated_at = utils.get_current_utc_time()
    
    db.add(company)
    db.commit()
    db.refresh(company)
    
    return company

def update_company(db: Session, id: UUID, data: CompanyModel) -> Company:
    company = get_company_by_id(db, id)

    if company is None:
        raise ResourceNotFoundError()
    
    company.name = data.name
    company.description = data.description
    company.mode = data.mode
    company.rating = data.rating
 
    db.commit()
    db.refresh(company)

    return company

def delete_company(db: Session, id: UUID) -> None:
    company = get_company_by_id(db, id)

    if company is None:
        raise ResourceNotFoundError()
    
    isCompanyContainsUsers = is_company_contains_users(db, id)
    
    if isCompanyContainsUsers is True:
        raise InvalidInputError("Please delete all users belonging to this company before deletion")   
     
    db.delete(company)
    db.commit()

def is_company_contains_users(db: Session, company_id: UUID) -> None:
    user =  db.scalars(select(User).filter(User.company_id == company_id)).first()
       
    return user is not None