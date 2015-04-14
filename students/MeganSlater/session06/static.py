""" Question 1:
Can I use a static method to count the number of times
any particular class has been initiated?
"""


class Spam(object):
    """class counts number of times class was used.
    Could add more features to this class if desired"""
    numInstances = 0

    def __init__(self):
            Spam.numInstances += 1

    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)
