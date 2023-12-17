# PyCookieCutter
A CookieCutter template to help start new Python projects the right way. 

## Pre-Requisites
Generating and running projects using this template require `cookiecutter` and `pyenv` to be available in your system
interpreter. These can be installed from PyPI and Homebrew respectively.

```shell
# Install pre-requisites:
brew update
brew install pyenv 
python3 -m pip install cookiecutter
```

## Usage
```shell
# Create new project from this template:
cookiecutter https://github.com/epikulski/pycookiecutter
```

## Features:
* Python version management with [pyenv](https://github.com/pyenv/pyenv).
* Provision virtual environment with [venv](https://docs.python.org/3/library/venv.html).
* Manage and pin dependencies with [pip-tools](https://github.com/jazzband/pip-tools).
* Configures a local dev install of the library under development in editable mode.
* Support for absolute imports throughout the project, including the test suite. 
* Adds a console script for the library's default entrypoint.
* Includes a Makefile with run configurations for linting, testing, building, and publishing to PyPI (or Artifactory). 

## Managing Python Dependencies
Templated projects contain two files for tracking python dependencies: `requirements.in` and `requirements.dev.in`.
These are used by [pip-compile](https://github.com/jazzband/pip-tools) to generate `requirements.txt` and 
`requirements.dev.txt`, which should not be edited directly.

The `dev` suffix corresponds to dependencies that are only relevant for local development. The development requirements
file is constrained by the production requirements file, to avoid impossible combinations of packages.

## Notes
This package is a template based on my personal preference for setting up local dev environments for Python library
development. After testing `poetry` and other tools, I've found that using Makefiles with `setuptools` to be the most 
simple and reliable for reproducibly creating a local dev environment from scratch. 