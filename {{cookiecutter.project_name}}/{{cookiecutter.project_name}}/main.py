"""
{{ cookiecutter.project_name }}.main

Contains entrypoints for the library.
"""
import logging

logger = logging.getLogger(__name__)

def entrypoint():
    """Default entrypoint for newproject"""
    logger.debug("Executing {{ cookiecutter.project_name }} entrypoint.")
    print("Welcome to {{ cookiecutter.project_name }}")
