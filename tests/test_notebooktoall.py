#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `notebooktoall` package."""

import pytest
import requests
import os

from notebooktoall import notebooktoall


#@pytest.fixture
#def import_export():
#    """Sample pytest fixture.

#    See more at: http://doc.pytest.org/en/latest/fixture.html
#    """
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_ouptuts_html_file():
    """Sample pytest test function with the pytest fixture as an argument."""

    assert os.path.exists('mynb.html')
