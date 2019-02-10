from urllib.request import urlopen
import nbformat
from traitlets.config import Config

# 1. Import the exporter
from nbconvert import HTMLExporter, PythonExporter, RSTExporter
from nbconvert.writers import FilesWriter

def build_files(
    url="http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb",
    notebook_name="my_converted_nb",
    exports=["html", "py"]
):

    try:
        response = urlopen(url).read().decode()
    except Exception as e:
        print(f"There was a problem: {e}")

    try:
        # Read a notebook from a string and return the NotebookNode object
        nb = nbformat.reads(response, as_version=4)
        exper(exports, nb, notebook_name)
    except Exception as e:
        print(f"There was a problem exporting or writing: {e}")
    return None

def exper(exps, nb_node, file_name):
    """
    export and write files
    exports(list of strings): name of valid nbconvert exporters
    """
    # TODO: Check that exports are valid types, let input valid types

    # export and write file.
    for exp in exps:
        if exp == "html":
            exporter = HTMLExporter()
        elif exp == "py":
            exporter = PythonExporter()
        elif exp == 'rst':
            exporter = RSTExporter()
        (body, resources) = exporter.from_notebook_node(nb_node)
        write_file = FilesWriter()
        write_file.write(output=body, resources=resources, notebook_name=file_name)
    return None
