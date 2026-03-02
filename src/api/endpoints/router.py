from fastapi import APIRouter

from .author import router as author_router
from .book_type import router as book_type_router
from .tag import router as tag_router

router = APIRouter()

# Include the tag router
router.include_router(tag_router, prefix="/tags", tags=["tags"])

# Include the author router
router.include_router(author_router, prefix="/author", tags=["author"])

# include the book typer router
router.include_router(book_type_router, prefix="/book-types", tags=["Book Type"])