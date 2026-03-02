from typing import Generic, List, TypeVar

from sqlmodel import Field, SQLModel

# Define a generic type variable
T = TypeVar("T")


class Page(SQLModel, Generic[T], table=False):
    """
    A page of results. This class is used to paginate the results of a query or response.
    """

    results: List[T] = Field(description="The list of results of size `page_size` and starting at `page`.")
    page: int = Field(default=1, description="The current page.")
    page_size: int = Field(default=50, description="The number of results per page.")
    total: int = Field(description="The total number of results.")
