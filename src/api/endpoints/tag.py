from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.api.deps import get_db 
from src.crud import tag as crud
from src.schemas import tag as schemas


router = APIRouter()


@router.get("", response_model=List[schemas.Tag])
def get_tags(db: Session = Depends(get_db)):
    """Get all tags."""
    tags = crud.get_all_tags(db)
    return tags
