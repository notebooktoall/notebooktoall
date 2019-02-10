from urllib.request import urlopen
import nbformat
from traitlets.config import Config

# 1. Import the exporter
from nbconvert import HTMLExporter
from nbconvert.writers import FilesWriter
from nbconvert.writers import StdoutWriter

url = "http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb"

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

    # Instantiate the exporter using the basic template.
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'

    # 3. Process the notebook we loaded earlier
    (body, resources) = html_exporter.from_notebook_node(jake_notebook)

    write_file = FilesWriter()
    write_file.write(output=body, resources=resources, notebook_name="mynb")


# TODO
# write output to file


except Exception as e:
    print(f"There was a problem exporting or writing: {e}")
