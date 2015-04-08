def fabonacci(n):
    """Return the nth value in the Fibonacci series."""

    val1, val2 = 0, 1
    for i in range(n):
        val1, val2 = val2, val1 + val2

    return val1

def lucas(n):
    """Return the nth value in the Lucas series."""

    val1, val2 = 2, 1
    for i in range(n):
        val1, val2 = val2, val1 + val2

    return val1

def sum_series(n, val1=0, val2=1):
    """Return the nth value for sum_series.
    Use optional parameters to produce other series.
    """


    for i in range(n):
        val1, val2 = val2, val1 + val2

    return val1


#Test if functions work properly
if __name__ == '__main__':
    assert fabonacci(3) == 2
    assert lucas(3) == 4
    assert sum_series(3, 2, 3) == 8
