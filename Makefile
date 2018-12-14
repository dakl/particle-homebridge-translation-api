run:
	watchmedo auto-restart python run.py --patterns="*.py" --recursive

unit-test:
	pytest -s .

lint:
	flake8 app/
	mypy --ignore-missing-imports app/

test: unit-test lint

build:
	docker build -t dakl/particle-homebridge-translation-api:latest .

push:
	docker push dakl/particle-homebridge-translation-api:latest