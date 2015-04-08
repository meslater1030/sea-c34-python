def printexcept():
    """what happens when you print an error? Does it contain a string?"""
    d = {'a': 1, 'b': 2, 'c': 3}
    try:
        d.sort()
        print(d)
    except AttributeError:
        print AttributeError

printexcept()

# result: "<type 'exceptions.AttributeError'>"
# there must be some other way to access the actual error message!


def exceptelif():
    """can you elif after an exception?"""
    d = 3
    e = input("enter number: ")
    try:
        f = d - e
    except ArithmeticError:
        print(u"you can't do that!")
    elif e > 0:
        print(u"the result is a positive number")
    else:
        print(u"the result is a negative number")

exceptelif()

# result: "SyntaxError: invalid syntax"
# seems the rest of the conditions have to be separate!
