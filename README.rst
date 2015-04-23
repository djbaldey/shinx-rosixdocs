=====
About
=====

RosixDocs - it's theme for Sphinx from Rosix projects.

.. figure:: screen.png
    :width: 100%
    :height: auto


=====
Usage
=====

.. code-block:: python

    # in your conf.py

    ...

    html_theme = 'default'

    #html_theme_path = []

    try:
        from rosixdocs import get_themes_path

        html_theme_path = [ get_themes_path() ]

        html_theme = 'html'

    except:
        pass

    ...
