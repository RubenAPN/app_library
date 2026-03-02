from fastapi import APIRouter, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError

from src.crud import book_type as crud
from src.db.transactional import DBSessionDep
from src.models.page import Page
from src.schemas import book_type as schemas

router = APIRouter()


@router.get("", response_model=Page[schemas.BookTypeResponse])
def get_book_types(
    db: DBSessionDep, 
    page: int = Query(1, ge=1, description="Current page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of results per page"),
    search: str = Query(None, description="Search term for domain names or codes")
):
    """
    Get all authors.
    """
    author = crud.get_all_book_type(db, page_size=page_size, page=page, search=search)
    return author

@router.get("/{book_type_id}", response_model=schemas.BookTypeResponse)
def get_book_type(book_type_id: int, db: DBSessionDep):
    try:
        return crud.get_book_type(db, book_type_id)
    except HTTPException as e:
        raise e

@router.post("", status_code=status.HTTP_201_CREATED)
def create(payload: schemas.BookTypeBase, db: DBSessionDep):
    try:
        return crud.create_book_type(db, payload)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book type already exists"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected server error"
        )
    
@router.put("/{book_type_id}", response_model=schemas.BookTypeResponse)
def update_book_type(book_type_id: int, updated_book_type: schemas.BookTypeUpdate, db: DBSessionDep):
    """
    Update a book type by ID.
    """
    try:
        return crud.update_book_type(db, book_type_id, updated_book_type)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected server error"
        )
    
@router.delete("/{book_type_id}")
def delete_book_type(book_type_id: int, db: DBSessionDep):
    """
    Delete a book type by ID.
    """
    try:
        crud.delete_book_type(db, book_type_id)
        return {"detail": "Book type deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected server error"
        )