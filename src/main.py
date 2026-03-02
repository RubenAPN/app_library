from fastapi import FastAPI

from src.api.router import router as api_router
from src.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)

app.include_router(api_router)

