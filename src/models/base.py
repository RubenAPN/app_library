from datetime import datetime
from datetime import timezone

from sqlalchemy.ext.declarative import declared_attr
from sqlmodel import Field
from sqlmodel import SQLModel

from src.utils.regex import to_snake_case

class Base(SQLModel, table=False):
    """
    This is the base class for all the transactional models that will be retrieved
    from the database. Here should be specified all the attributes. The target table
    name will be set based on the classname in snake case. Also, it will automatically
    generate the 'created_at' and 'updated_at' columns with the current timestamp in
    UTC timezone. The 'id' column will be the primary key of the table.
    """

    __name__: str

    id: int | None = Field(
        default=None,
        primary_key=True,
        index=True,
        description="The primary key of the record",
    )

    created_at: datetime = Field(
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
        description="The time the record was created",
    )

    updated_at: datetime = Field(
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc),
        },
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
        description="The last time the record was updated",
    )

    is_deleted: bool = Field(
        default=False,
        nullable=False,
        description="Flag to indicate if the record is deleted or not",
    )

    @declared_attr
    @classmethod
    def __tablename__(cls) -> str:
        """
        Generate the '__tablename__' attribute automatically in lowercase and
        snake-case style. Check the 'regex.to_snake_case' function in the utils
        module for further information of the transformation.
        """

        return to_snake_case(cls.__name__)