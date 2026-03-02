from typing import Optional

from pydantic import BaseModel


class BookTypeBase(BaseModel):
    book_type: str

    class Config:
        from_attributes = True


class BookTypeResponse(BaseModel):
    id: int
    book_type: str


class BookTypeUpdate(BaseModel):
    book_type: Optional[str] = None
