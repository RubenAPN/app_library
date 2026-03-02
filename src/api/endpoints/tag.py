from typing import List

from fastapi import APIRouter

from src.crud import tag as crud
from src.db.transactional import DBSessionDep
from src.schemas import tag as schemas

router = APIRouter()


@router.get("", response_model=List[schemas.Tag])
def get_tags(db: DBSessionDep):
    """Get all tags."""
    tags = crud.get_all_tags(db)
    return tags
