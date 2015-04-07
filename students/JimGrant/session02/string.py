import sys


def question01():
    """Answer the question: is joining a split string with an empty string equal to the original string?"""
    print("Question 1: Is joining a split string with an empty string equal to the original string?")

    teststring = "This is a test of the emergency string splitting system."
    joinedstring = "".join(list(teststring))

    if joinedstring == teststring:
        print("Yes!")
    else:
        print("No! Compare the two below:")
        print("Original string: {}".format(teststring))
        print("Joined string: {}".format(joinedstring))


def question02():
    """Answer the question: Is input() risky due to the possibility of code injection?
    The Session 3 notes has raw_input(), but I found input() as well. I read the doc on it and um...
    """
    print("Question 2: Is input() risky due to the possibility of code injection?")

    try:
        testinput = input("Type eval('1 / 0'): ")
        print("Not risky! Maybe you're using Python 3?")
    except ZeroDivisionError:
        print("Yup. We probably shouldn't use input() for anything ever. Next question: why does it exist?")
    except:
        print("You probably tried a different expression. input() is still a bad idea.")


def question03():
    """Answer the question: Can I put integers directly into a string without conversion using .format()?"""
    print("Question 3: Can I put integers directly into a string without conversion using .format()?")

    try:
        teststring = "Yes, I put {} ints in this string! The other is {}.".format(2, 5)
        print(teststring)
    except:
        error = sys.exc_info()
        print("No! This causes the following exception:")
        print(error)


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()
