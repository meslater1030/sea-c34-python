########################################
# This is for Task 5 - Strings
#######################################

'''
This program has three different functions that illustrate some of the 
operations one can do to a string. 
'''



'''
Can you use .isalnum() by letter/number? What happens in 
a string with mixed aphanumerics and special characters?

The function alpha_numeric uses a for loop to go through a string
letter by letter (or character by character) to determine if it's an
alphanumeric. If not, it replaces the non-alphanumeric with nothing and 
returns the string without non-alphanumeric characters at the end
'''

def alpha_numeric(n):
        print n
        for element in n:
                if element.isalnum():
                        continue
                else:
                        n = n.replace(element,"")
        print n

#Tests
'''
alpha_numeric("!A!!") returns
!A!!
A

alpha_numeric("@@@...!!!>&#%@*!") returns
@@@...!!!>&#%@*!
###### There is nothing there! This is supposed to be empty since there were no alphanumerics.

alpha_numeric("kjfhhf!jfhg,...,lkifdjbf!") returns
kjfhhf!jfhg,...,lkifdjbf!
kjfhhfjfhglkifdjbf

alpha_numeric("strrrrriiiiinnnngggg")
strrrrriiiiinnnngggg
strrrrriiiiinnnngggg

'''





'''
Can one pull out solely letters and number separately?

The function letter_or_number goes through each element in a string,
determines if it's a letter or number, and then places the element in it's 
respective list. It skips special characters because they fail the tests.
I found out about .isdigit() through this!
'''

def letter_or_number(n):
        print n
        letters = []
        numbers = []

        for element in n:
                if element.isalpha():
                        letters.append(element)
                elif element.isdigit():
                        numbers.append(element)

        print "Letter list: ", letters
        print "Number list: ", numbers

#Tests
'''
letter_or_number("hello123 space  world") returns
hello123 space  world
Letter list:  ['h', 'e', 'l', 'l', 'o', 's', 'p', 'a', 'c', 'e', 'w', 'o', 'r', 'l', 'd']
Number list:  ['1', '2', '3']

letter_or_number("!!$DDOWMC**1134") returns
!!$DDOWMC**1134
Letter list:  ['D', 'D', 'O', 'W', 'M', 'C']
Number list:  ['1', '1', '3', '4']
'''





'''
Can you use the index from enumerating as a test in a function?

Yes! The function upper_lower_split takes in a string, preferably a sentence.
It then splits the string by spaces and enumerates over each index and element after the split.
If the index is even, the element (word) has an .upper() operater applied, odd has a .lower()
applied. Once upper/lower is applied, it is appended to a list (temp_list.
Once complete, the elements in temp_list are joined with a space in between
'''

def upper_lower_split(n):

    temp_list = []

    for i, element in enumerate(n.split(" ")):
        if i % 2 == 0:
            temp_list.append(element.upper())
        else:
            temp_list.append(element.lower())


    print " ".join(temp_list)

#Test
'''
upper_lower_split("Hello my name is Kim and I like to dance and eat enchiladas!") returns
HELLO my NAME is KIM and I like TO dance AND eat ENCHILADAS!
'''
        
