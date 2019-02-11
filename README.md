[![Build Status](https://travis-ci.org/notebooktoall/notebooktoall.svg?branch=master)](https://travis-ci.org/notebooktoall/notebooktoall) [![Coverage Status](https://coveralls.io/repos/github/notebooktoall/notebooktoall/badge.svg?branch=master)](https://coveralls.io/github/notebooktoall/notebooktoall?branch=master)

# NotebookToAll
The coolest way to turn a Jupyter Notebook into sharable files. 

Turn your Jupyter Notebook into a .py executable file and an .html file with a one-line command. You can create both or either file type at the same time! Under the hood, this package uses Jupyter nbconvert.

# Quick Start

## Install
Install from PyPI with pip.

## Use

Make sure your notebook doesn't have magic commands in it if you want to create an executable .py script.

```
import notebooktoall from notebooktoall as nb

transform_notebooks(
    url="my_jupyter_notebook.ipynb",
    file_name="my_desired_output_file_base_name",
    export_list=["html", "py"]
    )

```

Run your code and your .html and .py files should appear be in your current working directory.

See the full docs at ReadTheDocs.

Get involved! We welcome issues, documentation and code improvements. See contributing. 

