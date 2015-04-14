#!/usr/bin/env python

import pytest

import testing


def test_error():
    a = 16
    assert testing.error(a) == "16 Horses"
