=============
NotebookToAll
=============


.. image:: https://img.shields.io/pypi/v/notebooktoall.svg
        :target: https://pypi.python.org/pypi/notebooktoall

.. image:: https://img.shields.io/travis/notebooktoall/notebooktoall.svg
        :target: https://travis-ci.org/notebooktoall/notebooktoall

.. image:: https://readthedocs.org/projects/notebooktoall/badge/?version=latest
        :target: https://notebooktoall.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/notebooktoall/notebooktoall/shield.svg
     :target: https://pyup.io/repos/github/notebooktoall/notebooktoall/
     :alt: Updates


The coolest way to turn a Jupyter Notebook into sharable files.

Turn your Jupyter Notebook into a .py executable file and an .html file with a one-line command. You can create both or either file type at the same time! Under the hood, this package uses Jupyter nbconvert.

nbconvert is great for command line transformations, but it takes a bit of work to use in a program. NotebookToAll to the rescue.

Quick Start
-----------

Install
_______

Install from PyPI.
`pip install notebooktoall`

Use
___

Make sure your notebook doesn't have magic commands in it if you want to create an executable .py script.::


    from notebooktoall.transform import transform_notebooks

    transform_notebooks(ipynb_file="my_jupyter_notebook.ipynb", export_list=["html", "py"])



Run your code and your .html and .py files should appear in your current working directory.

You can pass a Jupyter notebook url to transform_notebooks().

License
_______

* Free software: GNU General Public License v3

Docs
____

* Documentation: https://notebooktoall.readthedocs.io.


Credits:
________

The Cookiecutter_ `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
