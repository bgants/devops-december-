install:
	# install requirements
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# format
	black *.py itam/*.py
lint:
	# lint
	pylint --disable=R,C *.py itam/*.py
test:
	# test
	python -m pytest -vv --cov=itam itam/test_*.py --cov=main test_*py
build:
	# builds docker 
run:
	# runs
deploy:
	# deploys
all: install format lint test build run deploy
