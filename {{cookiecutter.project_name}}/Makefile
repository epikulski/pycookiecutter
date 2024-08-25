#!make
.PHONY: env lint test build docs publish clean
SHELL := /bin/bash

# Globals
PROJECT_NAME = {{ cookiecutter.project_name }}
VENV_PATH = .venv
VENV_PYTHON = $(VENV_PATH)/bin/python3
PYTHON_VERSION = {{ cookiecutter.python_version }}

all: env format lint test build docs

env:
	git init
	HOMEBREW_NO_AUTO_UPDATE=1 brew install pipx
	pipx install uv
	uv python pin $(PYTHON_VERSION)
	uv python install $(PYTHON_VERSION)
	uv venv $(VENV_PATH)
	uv pip compile --output-file requirements.txt pyproject.toml  # Build 'prod' dependencies.
	uv pip compile --output-file requirements.dev.txt --extra dev pyproject.toml  # Build 'dev' dependencies.
	uv pip sync requirements.txt requirements.dev.txt  # Install all (including dev) requirements to venv.
	uv pip install --editable .  # Install package under development.
	$(VENV_PATH)/bin/pre-commit install

lint:
	$(VENV_PYTHON) -m ruff check --fix $(PROJECT_NAME)
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

docs:
	# Build docs, fail build on warnings.
	$(VENV_PATH)/bin/sphinx-build \
		-W \
		--keep-going \
		./docs \
		docs/_build

build:
	uvx --from build pyproject-build --installer uv

publish: env build
	uvx twine upload --skip-existing --repository local dist/*

clean:
	rm -rf $(VENV_PATH)
	rm -rf **/__pycache__
	rm -rf **/.ipynb_checkpoints
	rm -rf $(REPO).egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf build
	rm -rf dist
