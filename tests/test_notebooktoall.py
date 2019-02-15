#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `notebooktoall` package."""
import pytest
import os
import nbformat
import notebooktoall.transform as nba

my_url = "http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb"
# default test notebook address

my_file = "my_tst.ipynb"
# default test notebook file path

my_file_types = ['html', 'py']
# file types for conversion into

# @pytest.fixture
# def build_file():
#    """test fixture to call function to create files from notebook"""


# Integration tests
def test_transform_notebook():
    """Test that output files are created when main function is called."""
    nba.transform_notebook(ipynb_file=my_url, export_list=my_file_types)
    file_name = my_url.rsplit('/', 1)[-1]
    file_base = file_name[:file_name.rfind('.')]

    """Check .html file exists from url."""
    assert os.path.exists(f'{file_base}.html')

    """Check .py file exists from url."""
    assert os.path.exists(f'{file_base}.py')

    nba.transform_notebook(ipynb_file=my_file, export_list=my_file_types)
    file_name = my_file.rsplit('/', 1)[-1]
    file_base = file_name[:file_name.rfind('.')]

    """Check html file exists from path."""
    assert os.path.exists(f'{file_base}.html')

    """Check .py file exists from path."""
    assert os.path.exists(f'{file_base}.py')


# Unit tests
def test_get_notebook():
    """Should return a NotebookNode object from a url."""
    my_nb_node = nba.get_notebook(my_url)
    assert type(my_nb_node) is nbformat.notebooknode.NotebookNode

    """Should return a NotebookNode object from a path."""
    my_nb_node = nba.get_notebook(my_file)
    assert type(my_nb_node) is nbformat.notebooknode.NotebookNode

    """Should raise an exception."""
    with pytest.raises(TypeError):
        my_nb_node = nba.get_notebook(5)

    """Should raise an exception."""
    # may require mocking
    # bad_url = "http:/funn.yfdf"
    # with pytest.raises(urllib2.URLError):
    #    my_nb_node = nba.get_notebook(bad_url)


def test_write_files():
    """Should run to completion."""
    my_nb_node = nba.get_notebook(my_url)
    nba.write_files(my_file_types, my_nb_node, file_name="my_file")

    """Should raise an exception."""
    bad_export_list = ['slides']
    my_nb_node = nba.get_notebook(my_url)
    nba.write_files(bad_export_list, my_nb_node, file_name="my_file2")
    assert pytest.raises(TypeError)
