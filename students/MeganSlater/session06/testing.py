"""Question 1:
Does Pytest only catch assertion errors or does it also catch
other errors in your code?
"""


def error(a):
    """This function will return an error if
    a is anything other than a string"""
    b = " Horses"
    return a + b
