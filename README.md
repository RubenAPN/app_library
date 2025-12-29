# app_library


## ORM
https://docs.sqlalchemy.org/en/20/orm/

## run api
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8081

## migración inicial 
alembic revision --autogenerate -m "initial migration" 

## realizar la migración 
alembic upgrade head

## bajar una versión en la migración
alembic downgrade -1