=====
Usage
=====

To use NotebookToAll in a project:


Make sure your notebook doesn't have magic commands in it if you want to create an executable .py script.

    .. code:: python

        from notebooktoall.transform import transform_notebook

        transform_notebook(ipynb_file="my_jupyter_notebook.ipynb", export_list=["html", "py"])



Run your program and your .html and .py files should appear in your current working directory.

You can also pass a Jupyter notebook URL to transform_notebooks().
