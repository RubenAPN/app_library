from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.models import book_type as models
from src.schemas import book_type as schemas


def get_all_book_type(db: Session, page: int = 1, page_size: int = 10, search: str = None):
    stmt = select(models.Type)
    if search:
        stmt = stmt.where(models.Type.name.ilike(f"%{search}%"))

    count_stmt = select(func.count()).select_from(stmt.subquery())
    total = db.execute(count_stmt).scalar_one()

    # Paginación
    offset = (page - 1) * page_size
    paged_stmt = stmt.offset(offset).limit(page_size)

    items = db.execute(paged_stmt).scalars().all()
    total_pages = (total + page_size - 1) // page_size
    return {
        "results": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages
    }


def get_book_type(db: Session, book_type_id: int):
    """Get a book type by ID."""
    stmt = select(models.Type).where(models.Type.id == book_type_id)
    book_type = db.execute(stmt).scalar_one_or_none()
    if not book_type:
        raise HTTPException(status_code=404, detail="Book type not found")
    return book_type


def create_book_type(db: Session, book_type: schemas.BookTypeBase):
    book_type = models.Type.model_dump(book_type)
    db.add(book_type)
    db.commit()
    db.refresh(book_type)
    return book_type


def update_book_type(db: Session, book_type_id: int, updated_book_type: schemas.BookTypeUpdate):
    stmt = select(models.Type).where(models.Type.id == book_type_id)
    book_type = db.execute(stmt).scalar_one_or_none()
    if not book_type:
        raise HTTPException(status_code=404, detail="Book type not found")
    update_data = updated_book_type.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book_type, key, value)
    db.commit()
    db.refresh(book_type)
    return book_type


def delete_book_type(db: Session, book_type_id: int):
    stmt = select(models.Type).where(models.Type.id == book_type_id)
    book_type = db.execute(stmt).scalar_one_or_none()
    if not book_type:
        raise HTTPException(status_code=404, detail="Book type not found")
    db.delete(book_type)
    db.commit()

