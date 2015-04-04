def lambda_loop(n, x):
    lambda_list = []
    for i in range(n):
        lambda_list.append(lambda x, e=i: x + e)
    for function in lambda_list:
        print(function(x))
lambda_loop(4, 5)
"""
e is a keyword variable.  We need
to set a keyword variable so that they're unique for
every function that's generated.

in general that would look like this:

[lambda variable, othervariable:
the function we want which should include both variables,
for every instance in in some iterable sequence]
"""


def lambda_constructor(n, x):
    lambda_list = [lambda x, e=i: x + e for i in range(n)]
    for function in lambda_list:
        print(function(x))
lambda_constructor(4, 5)
