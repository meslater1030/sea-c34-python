def function_builder(n):
    """Function returns list of n function such that each one, when called
    will return the input value, incremented by an increasing number using a
    for loop.
    """
    lambda_list = []
    for i in range(n):
        lambda_list.append(lambda x, e=i: x + e)
    return lambda_list

the_list = function_builder(20)[2](3)
print the_list

"""
notes for Megan:
e is a keyword variable.  We need
to set a keyword variable so that they're unique for
every function that's generated.

in general that would look like this:

[lambda variable, othervariable:
the function we want which should include both variables,
for every instance in in some iterable sequence]
"""


def lambda_constructor(n):
    """Function returns list of n function such that each one, when called
    will return the input value, incremented by an increasing number using a
    list consructor.
    """
    return [lambda x, e=i: x + e for i in range(n)]

the_list = function_builder(20)[2](3)
print the_list

