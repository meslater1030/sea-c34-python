from os import listdir
from os.path import isfile


def question01():
    """How do I print all the files in a directory?"""

    print("Question 1: How do I print all the files in a directory?")

    path = "../"
    for item in listdir(path):
        # directories will be printed without this conditional
        if isfile(path + item):
            print(item)

if __name__ == "__main__":
    question01()
