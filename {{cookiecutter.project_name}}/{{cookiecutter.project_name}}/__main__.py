"""
cookiecutter.__main__

Default entrypoint for library when it is called directly.
ex: `python3 -m {{ cookiecutter.project_name }}`
"""
import logging
import os

from {{ cookiecutter.project_name }}.main import entrypoint

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()

if __name__ == "__main__":
    logging.basicConfig(
        level=LOG_LEVEL,
        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s - ',
        handlers=[
            logging.StreamHandler()  # Log to console
        ]
    )

    entrypoint()
