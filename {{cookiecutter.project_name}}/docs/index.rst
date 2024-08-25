{{ cookiecutter.project_name }} documentation
=============================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

Examples
--------

You can include examples in your documentation, and assert that they are runnable like this:

.. testsetup:: *

   import {{ cookiecutter.project_name }}

Doctest example:

.. doctest::

   >>> {{ cookiecutter.project_name }}.main.entrypoint()
   Welcome to {{ cookiecutter.project_name }}

Test-Output example:

.. testcode::

   {{ cookiecutter.project_name }}.main.entrypoint()

This would output:

.. testoutput::

   Welcome to {{ cookiecutter.project_name }}

Contents
--------

.. toctree::

   api