from datetime import date
from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    last_name: str 
    birth_date: Optional[date]
    gender: str


class AuthorCreate(AuthorBase):
    pass

    class Config:
        from_attributes=True

