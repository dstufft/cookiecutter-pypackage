{{ cookiecutter.project_name }}
{% for _ in range(cookiecutter.project_name|length()) %}={% endfor %}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.png?branch=master
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master


{{ cookiecutter.project_short_description }}


Discussion
----------

If you run into bugs, you can file them in our `issue tracker`_.

You can also join ``{{ cookiecutter.irc_channel }}`` on Freenode to ask questions or get
involved.


.. _`documentation`: https://{{ cookiecutter.repo_name }}.readthedocs.org/
.. _`issue tracker`: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
.. _`cryptography-dev`: https://mail.python.org/mailman/listinfo/cryptography-dev
