#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import string


def test_startA():
    assert string.startA("I'm an excellent apple.") == 2
