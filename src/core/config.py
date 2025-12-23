from typing import Optional
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    PROJECT_NAME: str = 'Library App'
    PROJECT_VERSION: str = '0.1.0'
    PROJECT_DESCRIPTION: str = 'A simple library API built with FastAPI'
    DATABASE_URL: str

    class Config:
        env_file = '.env'

settings = Settings()