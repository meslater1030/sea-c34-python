"""How many words start with 'a' in a sentence?"""


def startA(str):
    str = str.split()  # split string into a list
    count = 0
    for i in str:
        firstLetter = i[0]
        if firstLetter.lower() == 'a':  # see if first letter is 'a'
            count += 1  # increment count
    return count

"""Is a user entered value a number?"""


def isNum(userInput):
    return userInput.isalnum()  # returns true if input is a number
isNum(raw_input("Enter a number: "))

"""Can a computer do mad libs?"""


def madLibs():
    verb = raw_input("Enter a verb ending in ing: ")
    noun = raw_input("Enter a plural noun: ")
    adj = raw_input("Enter an adjective: ")
    print('"There are too many %s %s on this %s plane!" he screamed.' % (verb, noun, adj))
madLibs()
