#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import iteration


def test_factorial():
    assert iteration.factorial(8) == 40320
