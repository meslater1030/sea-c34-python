"""What is the product of every number in a list?"""


def product(lst):
    total = 1
    for i in lst:
        total = total * i  # update total to multiply by each number in list
    return total

"""What is the factorial of any given integer?"""


def factorial(x):
    total = x
    x -= 1
    while x > 0:
        total = total * x  # update total to multiply by new x
        x -= 1  # deincriment x by one
    return total

"""Is this integer a prime number?"""


def is_prime(x):
    if x < 2:  # Neither one nor 0 are considered prime numbers
        return False
    if x == 2:  # Two is considered a prime number (Special case)
        return True
    for n in range(2, x-1):
        if x % n == 0:  # Check to see if number can be divided by anything except itself
            return False
        else:
            return True
