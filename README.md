[![Build Status](https://travis-ci.org/notebooktoall/notebooktoall.svg?branch=master)](https://travis-ci.org/notebooktoall/notebooktoall)
![latest](https://img.shields.io/pypi/v/notebooktoall.svg?style=flat) [![Coverage Status](https://coveralls.io/repos/github/notebooktoall/notebooktoall/badge.svg?branch=master)](https://coveralls.io/github/notebooktoall/notebooktoall?branch=master) [![Documentation Status](https://readthedocs.org/projects/pyup/badge/?version=latest)](https://pyup.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/notebooktoall/notebooktoall/shield.svg)](https://pyup.io/repos/github/notebooktoall/notebooktoall/)
![license](https://img.shields.io/pypi/l/notebooktoall.svg?style=flat)
![versions](https://img.shields.io/pypi/pyversions/notebooktoall.svg?style=flat)


# NotebookToAll
The coolest way to turn a Jupyter Notebook into sharable files.

Turn your Jupyter Notebook into a .py executable file and an .html file with a one-line command. You can create both or either file type at the same time! Under the hood, this package uses Jupyter nbconvert.

nbconvert is great for command line transformations, but it takes a bit of work to use in a program. NotebookToAll to the rescue.

# Quick Start

## Install
Install from PyPI.
`pip install notebooktoall`

## Use

Make sure your notebook doesn't have magic commands in it if you want to create an executable .py script.

```
from notebooktoall.transform import transform_notebooks

transform_notebooks(ipynb_file="my_jupyter_notebook.ipynb", export_list=["html", "py"])

```

Run your code and your .html and .py files should appear in your current working directory.

You can pass a Jupyter notebook url to transform_notebooks().

See the full docs at [ReadTheDocs](https://notebooktoall.readthedocs.io/en/latest/index.html).
