"""Question 1:
If my class inherits from object, do I have to define every special
method I want to be able to use or are special methods set to
some kind of default?
"""


class Rectangle(object):
    """define rectangle class with attributes of height
    and width as well as a special method of add"""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __add__(self, other):
        return Rectangle(self.height + other.height, self.width + other.width)

r1 = Rectangle(20, 30)
r2 = Rectangle(40, 50)


r3 = r1 + r2

# r3 = r1 * r2
# r3 = r1 + r2
# r3 = r1 / r2
# r3 = r1 // r2
# r3 = r1 ** r2

# all of these get errors.  Special methods are not defined.
