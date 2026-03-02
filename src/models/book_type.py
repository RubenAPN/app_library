from sqlmodel import Field

from src.models.base import Base


class Type(Base, table=True):
  book_type: str = Field(unique=True)