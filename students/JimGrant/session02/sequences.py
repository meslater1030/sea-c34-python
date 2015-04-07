import sys


def question01():
    """Answer the question: what happens if the end of my slice is greater than the beginning?"""
    print("Question 1: What happens if the end of my slice is greater than the beginning?")

    testlist = [1, 2, 3]
    upper_bound = len(testlist) - 1
    print("{} sliced from 0 to {} is: {}".format(testlist, upper_bound, testlist[0:upper_bound]))
    print("However, {} sliced from {} to 0 is: {}".format(testlist, upper_bound, testlist[upper_bound:0]))


def question02():
    """Answer the question: what happens if I try to use a float for a list index?"""
    print("Question 2: What happens if I try to use a float for a list index?")

    testlist = [1, 2, 3]
    testindex = 0.5

    try:
        print("Python thinks the {}th index of {} is: {}".format(testindex, testlist, testlist[0.5]))
    except:
        error = sys.exc_info()
        print("Trying to get the {}th index of {} causes this exception:".format(testindex, testlist))
        print(error)


def question03():
    """Answer the question: can I use list() to make a deep copy of a list?"""
    print("Question 3: Can I use list() to make a deep copy of a list?")

    testlist = [1, 2, 3, ["a", "b"]]
    testlist_copy = list(testlist)
    testlist[-1].pop()

    # if testlist_copy is shallow, "b" should have gotten popped off both lists
    if testlist == testlist_copy:
        print("No, list() creates a shallow copy of a provided list, just like [:]")
    else:
        print("Yes, list() creates a deep copy of a provided list")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()
