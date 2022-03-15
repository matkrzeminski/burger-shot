ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs

migrate:
	docker compose exec backend python3 manage.py migrate

makemigrations:
	docker compose exec backend python3 manage.py makemigrations

superuser:
	docker compose exec backend python3 manage.py createsuperuser

collectstatic:
	docker compose exec backend python3 manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect burger-src_postgres_data

db:
	docker compose exec postgres-db psql --username=admin --dbname=burger

shell_plus:
	docker compose exec backend python3 manage.py shell_plus

test:
	docker compose exec backend coverage run -m pytest

test-html:
	docker compose exec backend coverage html

flake8:
	docker compose exec backend flake8 .

black-check:
	docker compose exec backend black --check --exclude=migrations . --exclude=venv .

black-diff:
	docker compose exec backend black --diff --exclude=migrations . --exclude=venv .

black:
	docker compose exec backend black --exclude=migrations . --exclude=venv .

isort-check:
	docker compose exec backend isort . --check-only --skip env --skip migrations --skip venv

isort-diff:
	docker compose exec backend isort . --diff --skip env --skip migrations --skip venv

isort:
	docker compose exec backend isort . --skip env --skip migrations --skip venv


