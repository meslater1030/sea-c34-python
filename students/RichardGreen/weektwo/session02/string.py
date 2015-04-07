s = 'this is my string. how do you like it'
t = "Here,is,my,csv,string,oh,yeah"
p = 'good morning!'

'''Im going to define three separate functions to answer questions about the
strings above. My questions:
What do the strings look like in upper and lower characters.
What do my strings look like when I replace commas for tabs
What does my string look when converted tp ascii characters.'''


def case_print(x):
    '''definition of function: provide upper and lower case of the string
 arguments: a string'''
    print " Upper:"
    print x.upper()
    print "lower:"
    print x.lower()


def replace_comma_for_tabs(x):
    '''definition of function: convert commas to tabs arguments: a string'''
    tsv = '\t'.join(x.split(','))
    print "your updated string is:"
    print tsv


def ascii_my_string(x):
    '''definition of function: Print out the string in ASC II values.
arguments: a string x'''
    for i in x:
        print(ord(i), ' ')


if __name__ == "__main__":
    case_print(s)
    replace_comma_for_tabs(t)
    ascii_my_string(s)
