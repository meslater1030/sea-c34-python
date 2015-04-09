#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import html_render


def test_paragraph_output():
    p = html_render.P("I'm an excellent paragraph", style="bold", id="awesome")
    assert p.output == ["        <p style='bold'  id='awesome'>\n",
                        "           I'm an excellent paragraph\n", u"        </p>\n"]
