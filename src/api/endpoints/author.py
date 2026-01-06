from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.crud import author as crud
from src.schemas import author as schemas
from src.db.transactional import DBSessionDep


router = APIRouter()


@router.get("")
def get_author(db: DBSessionDep):
    """Get all authors."""
    author = crud.get_all_author(db)
    return author

@router.post("", status_code=status.HTTP_201_CREATED)
def create(payload: schemas.AuthorCreate, db: DBSessionDep):
    try:
        return crud.create_author(db, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Author already exists or invalid data")