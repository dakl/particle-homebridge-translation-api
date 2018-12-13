run:
	watchmedo auto-restart python run.py --patterns="*.py" --recursive

unit-test:
	pytest -s .

lint:
	flake8 .
	mypy .

test: unit-test lint
