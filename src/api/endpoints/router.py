from fastapi import APIRouter
from .tag import router as tag_router
from .author import router as author_router


router = APIRouter()

# Include the tag router
router.include_router(tag_router, prefix="/tags", tags=["tags"])

# Include the author router
router.include_router(author_router, prefix="/author", tags=["author"])