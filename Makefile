install:
	# install requirements
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# format
lint:
	# lint
test:
	# test
build:
	# builds docker 
run:
	# runs
deploy:
	# deploys
all: install format lint test build run deploy
