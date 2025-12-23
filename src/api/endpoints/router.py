from fastapi import APIRouter
from .tag import router as tag_router


router = APIRouter()

# Include the tag router
router.include_router(tag_router, prefix="/tags", tags=["tags"])
