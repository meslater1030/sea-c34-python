# Three questions from session 3 slides on strings

mystring = "Mr oh winding it enjoyed by between. The servants securing one material goodness her. Saw principles themselves ten are possession. So endeavor to continue cheerful doubtful we to. Turned advice the set vanity why mutual. Reasonably if conviction on be unsatiable discretion apartments delightful. Are melancholy appearance stimulated occasional entreaties end. Shy ham had esteem happen active county. Winding morning am shyness evident to. Garrets because elderly new manners however one village she."

username = raw_input('what is your name?')


def sayhello(name):
    """
    Print a greeting using the %s method.
    """
    return 'Hello, %s!' % name

print "Test for sayhello function:"
print sayhello('Mary')
print sayhello(username)


def sayhelloasfunction(name):
    """
    Print a greeting using the function method.
    """
    return 'Hello, {}!'.format(name)

print "Test for sayhelloasfunction:"
print sayhelloasfunction('Mary')
print sayhelloasfunction(username)


def sayhellotoyourmother(name):
    """
    Print a greeting to a name and another function-generated name.
    """
    momname = raw_input("Hello, {}! Who's your friend?".format(name))
    return 'Hi {}, hi {}'.format(name, momname)

print "Test for sayhellotoyourmother:"
print sayhellotoyourmother('Mary')
print sayhellotoyourmother(username)
