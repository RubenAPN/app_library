import logging
from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlmodel import Session
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL.unicode_string(), pool_pre_ping=True)


def get_db() -> Generator[Session, None, None]:
    """
    Creates a generator for a DB session and closes when use is done.
    """

    try:
        with Session(engine) as session:
            yield session
    except ValidationError as e:
        logging.error(f"Could not validate request {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not validate request",
        )
    finally:
        session.close()


DBSessionDep = Annotated[Session, Depends(get_db)]
