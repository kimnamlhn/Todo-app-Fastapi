from typing import List
from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_db_context, get_db_context
from models.company import CompanyModel, CompanyViewModel, SearchCompanyModel
from services.exception import ResourceNotFoundError, AccessDeniedError
from services import company as CompanyService
from schemas.user import User
from services import auth as AuthService

router = APIRouter(prefix="/company", tags=["Company"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[CompanyViewModel])
async def get_all_company(
    name: str = Query(default=None),
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=1, le=50, default=10),
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)
    ):
        if not user.is_admin:
            raise AccessDeniedError()
        
        conds = SearchCompanyModel(name, page, size)
        return CompanyService.get_company(db, conds)

@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def get_company_by_id(
    company_id: UUID,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)): 
      
    if not user.is_admin:
        raise AccessDeniedError()
    
    company = CompanyService.get_company_by_id(db, company_id)

    if company is None:
        raise ResourceNotFoundError()

    return company


@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompanyViewModel)
async def create_company(
    request: CompanyModel,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)):
    
    if not user.is_admin:
        raise AccessDeniedError()
    
    return CompanyService.add_new_company(db, request)


@router.put("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def update_company(
    company_id: UUID,
    request: CompanyModel,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)
    ):
    
    if not user.is_admin:
        raise AccessDeniedError()
    
    return CompanyService.update_company(db, company_id, request)


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(
    company_id: UUID,
    db: Session = Depends(get_db_context),
    user: User = Depends(AuthService.token_interceptor)
    ):
    
    if not user.is_admin:
        raise AccessDeniedError()
    
    CompanyService.delete_company(db, company_id)
