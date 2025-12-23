from sqlmodel import Field
from src.models.base import Base

class Tag(Base, table=True):
  name: str = Field(unique=True, index=True)
