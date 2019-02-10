#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `notebooktoall` package."""
import pytest
import requests
import os
from notebooktoall import notebooktoall

my_url = "http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb"
# test notebook address
my_note = "my_notebook"
# base name of converted files

@pytest.fixture
def build_file():
    """test fixture to call function to create files from notebook"""

    notebooktoall.build_files(
        url=my_url,
        notebook_name=my_note
    )

def test_ouptuts_html_file(build_file):
    """Does created html file exist?"""
    assert os.path.exists(f'{my_note}.html')

def test_ouptuts_py_file(build_file):
    """Does created pyton file exist?"""
    assert os.path.exists(f'{my_note}.py')
