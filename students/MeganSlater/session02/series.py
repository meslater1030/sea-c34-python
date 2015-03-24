def fibonacci(n):
    """Define the beginning of the sequence"""
    first = 0
    second = 1
    output = 0
    """Give a range for the loop"""
    remainder = n - 1
    """Return the appropriate number in the fibonacci sequence"""
    if n == 0:
        output = first
    elif n == 1:
        output = second
    else:
        for i in range(remainder):
            output = first + second
            first = second
            second = output
    return output


def lucas(n):
    """Define the beginning of the sequence"""
    first = 2
    second = 1
    output = 0
    """Give a range for the loop"""
    remainder = n - 1
    """Return the appropriate number in the lucas sequence"""
    if n == 0:
        output = first
    elif n == 1:
        output = second
    else:
        for i in range(remainder):
            output = first + second
            first = second
            second = output
    return output


def sum_series(n, first=0, second=1):
    """Give a range for the loop"""
    remainder = n - 1
    output = 0
    """Return the appropriate number in the sequence"""
    if n == 0:
        output = first
    elif n == 1:
        output = second
    else:
        for i in range(remainder):
            output = first + second
            first = second
            second = output
    return output

if __name__ == "__main__":
    """check to make sure  each function returns the correct answer"""
    assert(fibonacci(7) == 13)
    assert(fibonacci(3) == 2)
    assert(lucas(5) == 11)
    assert(lucas(1) == 1)
    assert(sum_series(7) == 13)
    assert(sum_series(2, 1, 2) == 3)
