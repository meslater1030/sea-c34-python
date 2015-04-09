#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return 'Circle with radius: %.6f' % self.radius

    def __repr__(self):
        return 'Circle(' + str(self.radius) + ')'

    def __add__(self, new):
        return Circle(self.radius + new.radius)

    def __mul__(self, new):
        return Circle(self.radius * new)

    def __cmp__(self, new):
        return self.radius - new.radius

    def __ne__(self, new):
        return self.radius != new.radius
