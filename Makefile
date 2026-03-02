# ===============================
# Configuración
# ===============================
APP_NAME=fastapi_app
APP_MODULE=src.main:app
HOST=0.0.0.0
PORT=8000
ENV=.env

PYTHON=python3
POETRY=poetry

# ===============================
# Ayuda
# ===============================
.PHONY: help
help:
	@echo "Comandos disponibles:"
	@echo "  make install        → Instala dependencias"
	@echo "  make run            → Levanta la API en modo desarrollo"
	@echo "  make test           → Ejecuta tests"
	@echo "  make lint           → Ejecuta linters"
	@echo "  make lint-file      → Ejecuta linters sobre un archivo"
	@echo "  make format         → Formatea el código"
	@echo "  make shell          → Abre shell con entorno Poetry"
	@echo "  make clean          → Limpia archivos temporales"

# ===============================
# Instalación
# ===============================
.PHONY: install
install:
	pip install -q poetry==1.7.1
	$(POETRY) install

# ===============================
# Ejecutar aplicación
# ===============================
.PHONY: run
run:
	poetry run uvicorn $(APP_MODULE) --port 8084 --host 0.0.0.0 --log-level=info --reload --env-file .env

# ===============================
# Testing
# ===============================
.PHONY: test
test:
	$(POETRY) run pytest -v

# ===============================
# Calidad de código
# ===============================
.PHONY: lint
lint:
	$(POETRY) run isort .
	$(POETRY) run ruff check .


.PHONY: lint-file
lint-file:
	@test -n "$(FILE)" || (echo "Usage: make lint-file FILE=path/to/file.py" && exit 1)
	$(POETRY) run isort $(FILE)
	$(POETRY) run ruff check $(FILE)


.PHONY: format
format:
	$(POETRY) run isort .
	$(POETRY) run ruff check --fix .
	$(POETRY) run ruff format .

.PHONY: format-file
format-file:
	@test -n "$(FILE)" || (echo "Usage: make format-file FILE=path/to/file.py" && exit 1)
	$(POETRY) run isort $(FILE)
	$(POETRY) run ruff check --fix $(FILE)
	$(POETRY) run ruff format $(FILE)

# ===============================
# Utilidades
# ===============================
.PHONY: shell
shell:
	$(POETRY) shell

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .ruff_cache