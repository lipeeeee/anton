"""Pytest testing

This Module contains all testing done automatically in each
git push by pytest
"""

import pytest

def inc(x):
    return x + 1

def test_fun():
    assert inc(2) == 3