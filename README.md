# app_library


## migración inicial 
alembic revision --autogenerate -m "initial migration" 

## realizar la migración 
alembic upgrade head

## bajar una versión en la migración
run alembic downgrade -1