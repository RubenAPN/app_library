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

pasos:

Siempre iniciar la bd
1.- poetry shell es para inicializar el ambiente virtual
2.- poetry install instalar dependencias.
3.- realizar migración(alembic upgrade head)(agregar a bd).
4.- migración inicial (alembic revision --autogenerate -m "")(para agregar cambios a migración)
5.- bajar una versión en la migración (alembic downgrade -1)(se utiliza para volver a una version de migración atrás en la bd por si quieres realizar cambios y no crear una migración nueva). 

para crear y cambiarse a la rama inmediatamente
git checkout -b feat/add_author main

crear rama
git branch feat/add_author main

cambiarse a una rama
git checkout feat/add_author