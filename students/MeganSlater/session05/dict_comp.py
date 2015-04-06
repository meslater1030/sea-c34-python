def step1():
    """print string from dictionary"""
    food_prefs = {"name": u"Megan",
                          u"city": u"Seattle",
                          u"cake": u"chocolate",
                          u"fruit": u"raspberries",
                          u"salad": u"chef salad",
                          u"pasta": u"mac and cheese"}

    print(u"{name} is from {city}, and she likes {cake}, {fruit}, {salad},"
          "and {pasta}.".format(**food_prefs))
step1()


def step2():
    """build dictionary that matches hex values with the appropriate base 10 value
     with list comprehension"""
    print(dict(zip(range(16),
          map(lambda x: hex(x), range(16)))))
step2()


def step3():
    print({key: value for key, value in zip(range(16),
          map(lambda x: hex(x), range(16)))})
step3()


def step4():
    """build dictionary that matches the key of the existing dictionary with
    the number of a's in the value of the old dictionary"""
    food_prefs = {"name": u"Megan",
                          u"city": u"Seattle",
                          u"cake": u"chocolate",
                          u"fruit": u"raspberries",
                          u"salad": u"chef salad",
                          u"pasta": u"mac and cheese"}
    food_a = {key: value.count('a') for key, value in food_prefs.iteritems()}
    print(food_a)
step4()


def step5a():
    """build three separate sets using three separate dictionary comprehensions
    that yields all numbers between 0 and 20 divisible by a particular number.
    """
    s2 = {x for x in range(21) if x % 2 == 0}
    s3 = {x for x in range(21) if x % 3 == 0}
    s4 = {x for x in range(21) if x % 4 == 0}
    print(s2)
    print(s3)
    print(s4)
step5a()


def step5b():
    """build three separate sets using one for loop
    that yields all numbers between 0 and 20 divisible by a particular number
    """
    sets = s2, s3, s4 = (set(), set(), set())

    for i, set_x in zip((2, 3, 4), sets):
        for j in range(21):
            if j % i == 0:
                set_x.add(j)

    print(s2)
    print(s3)
    print(s4)
step5b()


def step5c():
    """build three separate sets using one set comprehension
    that yields all numbers between 0 and 20 divisible by a particular number
    """
    s2, s3, s4 = ([{x for x in range(21) if x % i == 0} for i in range(2, 5)])
    print(s2)
    print(s3)
    print(s4)
step5c()

