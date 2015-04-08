#Question 1: Can two lists contain different object types can be concatenated?


def listAddition():
<<<<<<< HEAD
    """ 
    Concatenate two lists containing different object types
        Args: n/a

        Returns: n/a
=======
    """ Concatenate two lists containing different object types

    Args: 

    Returns: 

>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653
    """
    x = [1,2, 3]
    y = ['b', 'a', 'y']
    z = x + y
    print z

listAddition()

#Q2: Can an index be concatenated with a slice?

def printString():
<<<<<<< HEAD
    """ 
    Concatenate the index and slice of a string and print results

        Args: n/a

        Returns: n/a
=======
    """ Concatenates the index and slice of a string and print results

    Args:

    Returns:
>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653

    """
    s = "This is a string of letters"
    print s[5] + s[1:5]

printString()


#Q3: What is Duck typing?

def duckTyping():

<<<<<<< HEAD
    """ 
    Create classes Cow and Person containing the methods moo and chew

        Args: n/a

        Returns: n/a
=======
    """ Create classes Cow and Person containing the methods moo and chew

    Args:

    Returns:
>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653

    """

    class Cow: 
        def moo(self):
            print "Mooooooo!"
        def chew(self):
            print"Chomp, chomp, chomp"
    class Person:
        def moo(self):
            print "I'm mooing!"
        def chew(self):
            print "I'm chewing!"

    def on_the_farm(animal):
        animal.moo()
        animal.chew()

    on_the_farm(Cow())
    on_the_farm(Person())

duckTyping()





