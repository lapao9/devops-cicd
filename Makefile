.PHONY: up down logs test lint build push

# Desenvolvimento
up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f api

shell:
	docker compose exec api bash

db-shell:
	docker compose exec db psql -U taskuser -d taskdb

# Testes
test:
	docker compose run --rm api pytest tests/ -v

test-local:
	bash scripts/run-tests.sh

# Docker
build:
	docker build -t devops-cicd:local .

health:
	bash scripts/healthcheck.sh