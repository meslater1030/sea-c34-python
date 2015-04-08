def fibonacci(n):
    """return the value in the fibonacci series.

    Args:
        n:the fibonacci index to get the value.

    Returns:
        the fiboncci value of index n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def lucas(n):
    """return the value of the lucas numbers.

    Args:
        n: the lucas numbers index to get the value.

    Returns:
        the lucas number value of index n.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n - 1) + lucas(n - 2))


def sum_series(n, first_value=0, second_value=1):
    """ return the value from the fibonacci series or the lucas numbers or other
        series depending on the parameters.

    Args:
        n : the index of the series, first_value: the first value for the
        series to be produced, second_value: the second value for the series to
        be produced.

    Returns:
        the value of index n from the series to be produced.
    """
    if n == 0:
        return first_value
    elif n == 1:
        return second_value
    else:
        return (sum_series(n - 1, first_value, second_value) +
                sum_series(n - 2, first_value, second_value))

if __name__ == '__main__':
    assert fibonacci(3) == 2
    # This shows the value of index 3 of the fibonacci function equals to 2.
    assert lucas(4) == 7
    # This shows the value of index 4 of the lucas number function equals to 7
    assert sum_series(3) == 2
    # This shows calling sum_series with no optional arguments produce number
    # from the fibonacci series
    assert sum_series(4, first_value=2, second_value=1) == 7
    # This shows calling sum_series with the optional arguments 2 and 1 will
    # produce values from the lucas numbers.
    assert sum_series(2, first_value=4, second_value=5) == 9
    # This shows calling sum_series with other values for the optional
    # parameters will produce other series.
