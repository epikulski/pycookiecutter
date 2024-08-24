# PyCookieCutter
A CookieCutter template to help start new Python projects the right way. 

## Pre-Requisites
Generating and running projects using this template require `pipx` and `cookiecutter` to be available in your system
interpreter. These can be installed from Homebrew.

```shell
# Install pre-requisites:
brew install pipx
pipx install cookiecutter
```

## Usage
```shell
# Create new project from this template:
cookiecutter https://github.com/epikulski/pycookiecutter
```

## Features:
* Python version, venv, and dependency management with [uv](https://github.com/astral-sh/uv).
* Configures a local dev install of the library under development in editable mode.
* Support for absolute imports throughout the project, including the test suite. 
* Adds a console script for the library's default entrypoint.
* Includes a Makefile with run configurations for linting, testing, building, and publishing to PyPI (or Artifactory). 

## Managing Python Dependencies
Templated projects contain two files for tracking python dependencies: `requirements.in` and `requirements.dev.in`.
These are used by [uv](https://github.com/astral-sh/uv) to generate `requirements.txt` and 
`requirements.dev.txt`, which should not be edited directly.

The `dev` suffix corresponds to dependencies that are only relevant for local development. The development requirements
file is constrained by the production requirements file, to avoid impossible combinations of packages.
