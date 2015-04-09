#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import html_render


def test_paragraph_output():
    a = html_render.A("www.google.com", "Google")
    assert a.output == '<a href="www.google.com">Google</a> '
