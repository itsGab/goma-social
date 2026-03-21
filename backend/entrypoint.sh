#!/bin/sh
set -e

echo "Rodando migrações do Alembic..."
uv run alembic upgrade head

echo "Iniciando Uvicorn..."
exec uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
