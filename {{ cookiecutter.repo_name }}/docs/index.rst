Welcome to {{ cookiecutter.project_name }}
==========={% for _ in range(cookiecutter.project_name|length()) %}={% endfor %}

{{ cookiecutter.project_short_description }}

Installation
------------
You can install {{ cookiecutter.project_name }}`` with ``pip``:

.. code-block:: console

    $ pip install {{ cookiecutter.repo_name }}

.. toctree::
    :maxdepth: 2

    development/index
    security
