"""Question 1:
Can I set a property to delete more than itself when deleted?
"""


class C(object):
    def __init__(self, x=5, y=10):
        self._x = x
        self.y = y

    def _getx(self):
        return self._x

    def _setx(self, value):
        self._x = value

    def _delx(self):
        del self._x
        del self.y
    x = property(_getx, _setx, _delx, doc="docstring")

c = C()
del c.x
print(c.y)
