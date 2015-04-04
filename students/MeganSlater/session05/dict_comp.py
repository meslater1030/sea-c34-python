def step1():
    # this is for step 1
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
    print(dict(zip(range(16),
          map(lambda x: hex(x), range(16)))))
step2()


def step3():
    print({key: value for key, value in zip(range(16),
          map(lambda x: hex(x), range(16)))})
step3()


"""
def Jimstep5():
    s2, s3, s4 = [{n for n in range(21) if n % i == 0} for i in range(2, 5)]
    print(s2)
    print(s3)
    print(s4)


def jonstep5b():
    sets = s2, s3, s4 = (set(), set(), set())

    for i, set_x in zip((2, 3, 4), sets):
        for j in range(21):
            if j % i == 0:
                set_x.add(j)
    The rest is Megan's for part c

    [set_x.add(j) for i, set_x in zip((2, 3, 4), sets)
     for j in range(21) if j % i == 0]
    print(s2)
    print(s3)
    print(s4)
"""
