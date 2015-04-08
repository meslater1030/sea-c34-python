#####################################################
# This is for Task 5- Iterations
#################################################
'''
The functions in this program go over loops. I tried in the first two to create
images, then moved on to some fun with lists.
'''


'''
Can I print out a right triange using a loop?

The function right_triange prints out n amount of lines, all increasing by 1.
I went from range(1, n+1) in order to not have an empty row
'''

def right_triangle(n):
        for i in range(1, n+1):
                print "*" * i

#Tests
'''
right_triangle(3) returns
*
**
***
right_triangle(7) returns 
*
**
***
****
*****
******
*******
'''


'''
Can I make a more difficult equilateral triange? How does raw_input work?

The function equi_triange asks the user for two things, the number of rows
and a character in order to make the triangle. It then uses a for loop to 
print the correct series of characters and spaces
'''

def equi_triangle():
        height = int(raw_input("What height would you like the equilateral triangle? "))
        character = raw_input("What character should we use to make the triangle? ")
        space_char = " "
        
        for i in range(height):
            print (space_char * (height - i - 1)) + ((character + space_char) * (i+1))
        
#Tests
'''
After inputting a random height of 7 and a character of #:
equi_triangle() returns
      #
     # #
    # # #
   # # # #
  # # # # #
 # # # # # #
# # # # # # #
'''


'''
Can you toggle a boolean in a loop?

In the function numbers_between_neg1, a list of numbers is given. The function searches for a 
certain number, in this case -1 and appends the numbers between the first -1 and a successive -1
to a new list. It uses a boolean to determine if the number fits the "between -1s" criteria.
'''

def numbers_between_neg1(orig_list):
    between_list = []
    flag = False

    for i in orig_list:
        if i == -1 and flag == False:
            flag = True
        elif i == -1 and flag == True:
            flag = False
        elif flag == True:
            between_list.append(i)

    print between_list

#Tests
'''
numbers_between_neg1([6,4,-1,3,6,7,2,-2,1,56,-1,45,3]) returns
[3, 6, 7, 2, -2, 1, 56]

numbers_between_neg1([1,5,6,3,4]) returns
[]

numbers_between_neg1([4,3,-1,5,9,11]) returns
[5, 9, 11]
'''
