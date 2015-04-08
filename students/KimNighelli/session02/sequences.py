############################################
# This is for Task 5 - Sequences
###########################################

'''

This program goes over a series of questions that I had on the subject of sequences. 
I guess I didn't have too many question about the concepts- I more wanted to see the 
operations in action. 
'''




'''
Can I print out a string that is gradually reduced on each side?

In the function reduce_length, I go over two concepts- length and splicing.
The function is meant to take a string and print out the string with 1 less, 
then 2 less, etc. The length is to determine how many iterations one can do.

'''
def reduce_length(n):
    max_iteration = len(n)/2

    print n
    for i in range(1, max_iteration+1):
        print n[i:-i]

# Tests
'''
reduce_length("adda") returned:
dda
dd

reduce_length("tententen") returned
tententen
entente
ntent
ten
e
'''






'''
Can I specify what intervals I want to splice at?

The function every_other simply prints out every other letter. This uses splicing
but introduces the additional, optional argument of step
'''
def every_other(n):

    print "Original string: ", n
    print "String with every other letter: ", n[::2]

# Test
'''
every_other("abcdefghijklmnopqrstuvwxyz") returned

Original string:  abcdefghijklmnopqrstuvwxyz
String with every other letter:  acegikmoqsuwy
'''
    





''' 
Could I use splicing to test if a string is a pallindrome?

The function pallindrome tests to see if a string is a pallindrome- 
It ask if a string is equal to the same string spliced backwards (the step
of -1).
'''

def pallindrome(x):
        if x == x[::-1]:
                print "%s is a pallindrome!" % (x)
        else:
               print "%s is not a pallindrome" % (x)

#Test
'''
pallindrome("abcba") returns
abcba is a pallindrome!

pallindrome("definitelyNot") returns 
definitelyNot is not a pallindrome
'''
