PROJECT_NAME=people_microservice

default: run

tests:
	pipenv run pytest --cov=. --cov-report html

run:
	pipenv run python main.py