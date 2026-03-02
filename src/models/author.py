from datetime import date

from sqlmodel import Field

from src.models.base import Base


class Author(Base, table=True):
  name: str = Field(unique=True, index=True)
  last_name: str = Field(unique=True, index=True)
  birth_date: date = Field(nullable=True)
  gender: str = Field(nullable=False)