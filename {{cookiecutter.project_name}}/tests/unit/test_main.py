from {{ cookiecutter.project_name }}.main import entrypoint


def test_entrypoint():
    entrypoint()
