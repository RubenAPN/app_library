from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models import tag as models


def get_all_tags(db: Session):
    return db.query(models.Tag).all()


def get_tag(db: Session, tag_id: int):
    """Get a tag by ID."""
    tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag