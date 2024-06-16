.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: shell
shell:
	poetry run python manage.py shell

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: serve
serve:
	poetry run mkdocs serve

.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest -rS -n auto --show-capture=no

.PHONY: install-precommit
install-precommit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: docker-up
docker-up:
	docker compose up
