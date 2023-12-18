#!make
.PHONY: env lint test build publish clean
SHELL := /bin/bash

# Globals
PROJECT_NAME = {{ cookiecutter.project_name }}
VENV_PATH = .venv
VENV_PYTHON = $(VENV_PATH)/bin/python3


all: env format lint test build

env:
	pyenv install --skip-existing
	pyenv exec python3 -m venv $(VENV_PATH)
	$(VENV_PYTHON) -m pip install --upgrade pip pip-tools setuptools # Install "fundamental" dependencies
	$(VENV_PYTHON) -m piptools compile --output-file requirements.txt pyproject.toml  # Build 'prod' dependencies.
	$(VENV_PYTHON) -m piptools compile --output-file requirements.dev.txt --extra dev pyproject.toml  # Build 'dev' dependencies.
	$(VENV_PYTHON) -m piptools sync requirements.txt requirements.dev.txt  # Install all (including dev) requirements to venv.
	$(VENV_PYTHON) -m pip install --editable .  # Install package under development.
	$(VENV_PYTHON) -m pip show $(PROJECT_NAME)

lint:
	$(VENV_PYTHON) -m ruff check $(PROJECT_NAME)
	$(VENV_PYTHON) -m mypy $(PROJECT_NAME)

format:
	$(VENV_PYTHON) -m ruff format $(PROJECT_NAME)

test-unit:
	$(VENV_PYTHON) -m pytest --junitxml=build/reports/unit.xml -o junit_family=xunit2 tests/unit

test-int:
	$(VENV_PYTHON) -m pytest --junitxml=build/reports/int.xml -o junit_family=xunit2 tests/int

test-all:
	$(VENV_PYTHON) -m pytest --junitxml=build/reports/all.xml -o junit_family=xunit2 tests

test: test-all

build:
	$(VENV_PYTHON) -m build --sdist .

publish: env build
	$(VENV_PYTHON) -m twine upload --skip-existing --repository local dist/*

clean:
	rm -rf $(VENV_PATH)
	rm -rf **/__pycache__
	rm -rf **/.ipynb_checkpoints
	rm -rf $(REPO).egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf build
	rm -rf dist
