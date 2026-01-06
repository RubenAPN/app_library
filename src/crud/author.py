from sqlalchemy.orm import Session
from src.models import author as models
from src.schemas import author as schemas
from fastapi import HTTPException


def get_all_author(db: Session):
    return db.query(models.Author).all()


def get_author(db: Session, author_id: int):
    """Get a authors by ID."""
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

def create_author(session: Session, payload: schemas.AuthorCreate):
    author = models.Author.model_validate(payload)
    session.add(author)
    session.commit()
    session.refresh(author)
    return author