# PyCookieCutter
A CookieCutter template to help start new Python projects the right way. 

## Usage
```shell
python3 -m pip install cookiecutter
cookiecutter https://github.com/epikulski/pycookiecutter
```

## Features:
* Provision virtual environment with `venv`.
* Configures a local dev install of the library under development in editable mode.
* Support for absolute imports throughout the project, including the test suite. 
* Adds a console script for the library's default entrypoint.
* Includes a Makefile with run configurations for linting, testing, building, and publishing to PyPI (or Artifactory). 

## Notes
This package is a template based on my personal preference for setting up local dev environments for Python library
development. After testing `poetry` and other tools, I've found that using Makefiles with `setuptools` to be the most 
simple and reliable for reproducibly creating a local dev environment from scratch. 