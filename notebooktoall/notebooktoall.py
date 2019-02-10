def build_files(
    url="http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb",
    notebook_name="my_converted_nb"
):
    from urllib.request import urlopen
    import nbformat
    from traitlets.config import Config

    # 1. Import the exporter
    from nbconvert import HTMLExporter
    from nbconvert import PythonExporter
    from nbconvert.writers import FilesWriter

    try:
        response = urlopen(url).read().decode()
        response[0:5] + '...'
        #print(response)
    except Exception as e:
        print(f"There was a problem: {e}")

    try:
        # Read a notebook from a string and return the NotebookNode object as the given version.
        jake_notebook = nbformat.reads(response, as_version=4)
        jake_notebook.cells[0]

        # export and write html file.
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        (body, resources) = html_exporter.from_notebook_node(jake_notebook)
        write_file = FilesWriter()
        write_file.write(output=body, resources=resources, notebook_name=notebook_name)

        # export and write html file.
        py_exporter = PythonExporter()
        (body, resources) = py_exporter.from_notebook_node(jake_notebook)
        write_file = FilesWriter()
        write_file.write(output=body, resources=resources, notebook_name=notebook_name)

    except Exception as e:
        print(f"There was a problem exporting or writing: {e}")
