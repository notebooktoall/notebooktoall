"""Transform Jupyter Notebook to executable python script and/or html file."""

from urllib.request import urlopen
import nbformat
from nbconvert import HTMLExporter, PythonExporter
from nbconvert.writers import FilesWriter


def get_notebooks(ipynb_file):
    """
    Convert Jupyter notebook from url or directory to a NotebookNode object.

    Args:
        ipynb_file (str): url or path of notebook

    Returns:
        NotebookNode object

    """
    try:
        if "http" in ipynb_file:
            ipynb_file = urlopen(ipynb_file).read().decode()
            notebook_node = nbformat.reads(ipynb_file, as_version=4)
        else:
            notebook_node = nbformat.read(ipynb_file, as_version=4)
        return notebook_node
    except Exception as e:
        print(f"There was a problem exporting the notebook: {e}")


def write_files(export_list, nb_node, file_name):
    """
    Export and write files from a notebook node.

    Args:
        export_list (list of strings) -- name of valid nbconvert exporters
        nb_node(nbformat node object) -- notebook to be my_converted
        file_name (str) -- base name of file to be written

    Returns:
        None

    """
    try:
        # export and write file.
        for export in export_list:
            if export == "html":
                exporter = HTMLExporter()
            elif export == "py":
                exporter = PythonExporter()

            (body, resources) = exporter.from_notebook_node(nb_node)
            write_file = FilesWriter()
            write_file.write(
                output=body,
                resources=resources,
                notebook_name=file_name
            )
    except Exception as e:
        print(f"There was a problem exporting writing the file(s): {e}")
    return None


def transform_notebooks(
    ipynb_file,
    export_list=["html", "py"]
):
    """
    Transform notebooks to specified document types.

    Args:

        ipynb_file (str): url or path of Jupyter notebook to be converted
        export_list(list of strs): output file types. Defaults: html, py.

    Returns:
        None

    """
    file_name = ipynb_file.rsplit('/', 1)[-1]
    file_name = file_name[:file_name.rfind('.')]

    nb_node = get_notebooks(ipynb_file)
    write_files(export_list, nb_node, file_name)
    return None

# TODO:
# Check that ipynb and export_list types are valid
# possible feature: return the created objects or a message
