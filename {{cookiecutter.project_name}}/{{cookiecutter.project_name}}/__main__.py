"""
cookiecutter.__main__

Default entrypoint for library when it is called directly.
ex: `python3 -m {{ cookiecutter.project_name }}`
"""
from {{ cookiecutter.project_name }}.main import entrypoint

if __name__ == "__main__":
    entrypoint()