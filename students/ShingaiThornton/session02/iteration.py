#Q1: How does list enumeration work?
<<<<<<< HEAD

def listEnumerate():
    """ 
    Create and print an index for a list

         Args: n/a

         Returns: n/a
    
    """

=======
""" Create and print an index for a list

     Args: 

     Returns:
"""
def listEnumerate():
faowiejgawe
>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653
    flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip'] 
    print list(enumerate(flavors))

listEnumerate()



#Q2:  Can while loops be placed inside for loops?
<<<<<<< HEAD


def printNumbers():
    """ 
    Print all numbers between between 1 and 20 except for 5
     
        Args:

        Returns: numbers 
    """
=======
""" Print all numbers between in a rangeexcept for 5
     
     Args:

     Returns: numbers 
"""

def printNumbers():
>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653

    for x in xrange(20):
       
        while x != 5 :
            print x
            x = x + 1
            break

printNumbers()

 
<<<<<<< HEAD
=======

>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653
#Q3: How would I rewrite the for loop from the slides (starting on line 143) as a while loop?
"""
Print the numbers 25 - 50 using a while loop

<<<<<<< HEAD
Args: n/a

Returns: n/a
=======
Args:

Returns:
>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653
"""


def forAsWhileLoop():

    i = 1

    while i < 100:
        i = i + 1
       
        if i > 50:
            break
        if i < 25:
            continue
        print(i)    

<<<<<<< HEAD
forAsWhileLoop()
=======
forAsWhileLoop()




>>>>>>> eb1fcc6df394b5f849118de20c85ffd597e14653
