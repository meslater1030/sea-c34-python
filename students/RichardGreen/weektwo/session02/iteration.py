'''Lets make a sequence of numbers to iterate through'''

nums = range(25)

'''Next lets make a string of characters'''

s ='a b c d e f g h i j k l m n o p'


def print_second_num(s):
'''lets print the second value of each letter in the sequence and double it'''
	i = 0
	if i < len(s):
        	print 2*(s[i])
	i = i +2
 
def addnumbers(n):
''' instead of using the built in sum function lets use iteration to add the sequence together''' 
	sum =0
	for item in n:
        sum += item 
	print sum


def lookingforabc(s):
'''Lets display our sequence until we reach a user defined character. if we dont find it exit'''
   if item in s == 'abc':
   print TRUE
   else   
   print FALSE 



if __name__ == '__main__':
    # Do something interesting here
    # It will only happen when the module is run
