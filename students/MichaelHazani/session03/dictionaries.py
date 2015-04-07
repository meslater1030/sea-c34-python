def variablekey():
    """can a key be a variable?"""
    a = "myname"
    b = "hisname"
    d = {a: "George", b: "Charles"}
    print(d[a])

# variablekey()
# result: yes!


def dictorder():
    """can a dictionary be ordered by size?"""
    d = {1: 'a', 3: 'c', 2: 'b'}
    d.sort()
    print(d)
# dictorder()
# result: no! "AttributeError: 'dict' object has no attribute 'sort'"


def multivalue():
    """can a dictionary have more than one value per key?"""
    d = {1: "George", "Prince", "Male", 2: "Margaret", "Queen", "Lizard"}
    print(d)
# multivalue()
# result: no! "SyntaxError: invalid syntax"


def dictpluslist():
    """can lists be appended to dictionaries?"""
    d = {1: 'a', 2: 'b', 3: 'c'}
    lista = ['d', 'e', 'f']
    d.append(lista)
    print(d)

# dictpluslist()
# result: no! "AttributeError: 'dict' object has no attribute 'append'""
# Guess we'll have to use the "update" method for dicts.
