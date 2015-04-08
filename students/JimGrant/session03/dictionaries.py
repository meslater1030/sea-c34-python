from __future__ import print_function


def question01():
    """Can I use zip to do more than 2 loops at once?"""

    print("Question 1: Can I use zip to do more than 2 loops at once?")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]

    for i, j, k in zip(list1, list2, list3):
        print("{}, {}, {}".format(i, j, k))


def question02():
    """Will setdefault() replace the value if the value is None?"""

    print("Question 2: Will setdefault() replace the value if it is None?")
    d = {"key": None}
    d.setdefault("key", "something")

    if d["key"] == "something":
        print("Yes, setdefault() treats None as the value not existing.")
    elif d["key"] == None:
        print("No, a value of None is a value, and setdefault respects that.")
    else:
        print("I must not understand how this function works.")


def question03():
    """How are set.difference() and set.symmetric_difference() different?"""

    print("How are set.difference() and set.symmetric_difference() different?")
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}

    print("difference: {}".format(s1.difference(s2)))
    print("symmetric_difference: {}".format(s1.symmetric_difference(s2)))


def question04():
    """How is a frozen set different from a tuple?"""

    print("Question 4: How is a frozen set different from a tuple?")
    a_frozen_set = frozenset((1, 2, 3))
    a_tuple = (1, 2, 3)
    fs_dir = dir(a_frozen_set)
    tuple_dir = dir(a_tuple)

    print("Frozen Sets have the following methods that tuples don't:")
    for m in fs_dir:
        if m not in tuple_dir:
            print(m, end=" | ")

    print("\n")
    print("Tuples have the following methods that frozen sets don't:")
    for m in tuple_dir:
        if m not in fs_dir:
            print(m, end=" | ")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()
    print("")
    question04()
