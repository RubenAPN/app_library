from typing import Generator
from src.db.session import SessionLocal


def get_db() -> Generator:
    """Get a database session.

    Yields:
        Generator: A database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()