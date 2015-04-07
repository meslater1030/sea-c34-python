# Three questions from session 3 slides on sequences

mystring = "Mr oh winding it enjoyed by between. The servants securing one material goodness her. Saw principles themselves ten are possession. So endeavor to continue cheerful doubtful we to. Turned advice the set vanity why mutual. Reasonably if conviction on be unsatiable discretion apartments delightful. Are melancholy appearance stimulated occasional entreaties end. Shy ham had esteem happen active county. Winding morning am shyness evident to. Garrets because elderly new manners however one village she."


def howmany(x, string):
    """
    Determine how many times a single character occurs in a string.

    Args:
        x: the character to count
        string: the text to search

    Returns: a count of x
    """
    count = 0
    for i in string:
        if i == x:
            count = count + 1
    return count

print "Test for howmany function:"
print howmany('a', mystring)
print howmany('b', mystring)


def isin(x, string):
    """
    Determine if a given character occurs in a string, return boolean.
    """
    if x in string:
        return True
    else:
        return False

print "Test for isin function:"
print isin('a', mystring)
print isin('?', mystring)


def findword(x, string):
    """
    Determine if a given word occurs in a string, return boolean
    """
    if string.count(x) > 0:
        return True
    else:
        return False

print "Test for findword function:"
print findword('one', mystring)
print findword('wobbly', mystring)
