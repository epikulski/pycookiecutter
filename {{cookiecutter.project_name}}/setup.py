import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version="0.1.0",
    author="{{ cookiecutter.developer_name }}",
    author_email="{{ cookiecutter.developer_email }}",
    description="{{ cookiecutter.project_name }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    license="Proprietary",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_name }}={{ cookiecutter.project_name }}.main:entrypoint"
        ]
    },
)
