#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `notebooktoall` package."""
import pytest
import requests
import os
from notebooktoall import notebooktoall

my_url = "http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb"
# test notebook address
my_notebook = "my_notebook"
# base name of converted files
my_file_types = ['html', 'py']
# file types for conversion into

@pytest.fixture
def build_file():
    """test fixture to call function to create files from notebook"""
    nb_node = notebooktoall.get_notebooks(url=my_url)
    notebooktoall.write_files(my_file_types, nb_node, my_notebook)


def test_output_html_file(build_file):
    """check new html file exist"""
    assert os.path.exists(f'{my_notebook}.html')

def test_output_py_file(build_file):
    """check new python file exists"""
    assert os.path.exists(f'{my_notebook}.py')

#def test_get_notebooks():
#    """should return a NotebookNode object"""
