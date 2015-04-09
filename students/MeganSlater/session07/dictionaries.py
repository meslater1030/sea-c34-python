#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import dictionaries


def test_dict_by_value():
    d = {"key1": 1, "key2": 2, "key3": 3}
    dictionaries.dict_by_value(d, 3) == "key3"
