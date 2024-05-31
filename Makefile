.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

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
	poetry run pytest -rP
