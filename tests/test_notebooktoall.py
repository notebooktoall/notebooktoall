#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `notebooktoall` package."""
import pytest
import requests
import os
import nbformat
from notebooktoall import notebooktoall as nba

my_url = "http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb"
# default test notebook address

file_base = "my_new_file"
# base name of converted files

my_file_types = ['html', 'py']
# file types for conversion into

@pytest.fixture
def build_file():
    """test fixture to call function to create files from notebook"""
    nb_node = nba.get_notebooks(url=my_url)
    nba.write_files(my_file_types, nb_node, file_base)

# Integration tests
def test_transform_notebooks(build_file):
    """check new html file exist"""
    assert os.path.exists(f'{file_base}.html')
    assert os.path.exists(f'{file_base}.py')

# Unit tests
def test_get_notebook():
    """should return a NotebookNode object"""
    my_nb_node = nba.get_notebooks(my_url)
    assert type(my_nb_node) is nbformat.notebooknode.NotebookNode

    """should raise an exception"""
    bad_url = "htt:/funn.y"
    # my_nb_node = get_notebook(my_url)
    # assert raises an error


def test_write_files():
    """should run to completion"""
    my_nb_node = nba.get_notebooks(my_url)
    nba.write_files(my_file_types, my_nb_node, file_base)
