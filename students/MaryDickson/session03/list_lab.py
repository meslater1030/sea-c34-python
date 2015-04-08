#!/usr/bin/env python


def makelist():
    list = ["Apples", "Pears", "Oranges", "Peaches"]
    return list


def addfruit(newfruit, list):
    list.append(newfruit)
    return list


def indexfruit(list):
    indexnum = (int(raw_input("What number do you want to look up?"))) - 1
    while indexnum not in range(len(list)):
        indexnum = (int(raw_input("Sorry, that number doesn't exist.\n" +
        "Please choose a lower number. What number" +
        " do you want to look up?"))) - 1
    else:
        return list[indexnum]


def addfruitinsert(newfruit, list):
    list.insert(0, newfruit)
    return list


def addfruitplus(newfruit, list):
    newlist = [newfruit] + list
    return newlist


def findpfruits(list):
    pfruits = []
    for fruit in list:
        if fruit[0] == "p" or fruit[0] == "P":
            pfruits += [fruit]
    return pfruits


def badfruit(fruit, list):
    while fruit in list:
        list.remove(fruit)
    return list


def fixlist(list):
    yeslist = []
    nolist = []
    masterlist = []
    for fruit in list:
        if fruit.lower() in yeslist:
            masterlist.append(fruit.lower())
        elif fruit.lower() in nolist:
            pass
        else:
            ask = raw_input("Do you like " + str(fruit) + " ? Yes or No: ")
            while ask.lower() not in ['yes', 'y', 'n', 'no']:
                ask = raw_input("Sorry, I don't understand. Do you like " +
                    str(fruit) + " ? Yes or No: ")
            if ask.lower() == 'yes' or ask.lower() == 'y':
                yeslist.append(fruit.lower())
                masterlist.append(fruit.lower())
            elif ask.lower() == 'no' or ask.lower() == 'n':
                nolist.append(fruit.lower())
    return masterlist


def reverselistitems(list):
    reverselist = []
    for item in list:
        reverselist.append(item[::-1])
    return reverselist


def runprogram(mylist):
    # part 1
    newfruit = raw_input("What fruit would you like to add to the list?" )
    addfruit(newfruit, mylist)
    print mylist
    numfruit = indexfruit(mylist)
    print numfruit
    newfruit = raw_input("What fruit would you like to add" +
        "to the beginning of the list using the insert method?")
    addfruitinsert(newfruit, mylist)
    print mylist
    newfruit = raw_input("What fruit would you like to add" +
        "to the beginning of the list using the plus method?")
    mylist = addfruitplus(newfruit, mylist)
    print mylist
    print "Here are all your fruits that begin with a 'p': "
    print findpfruits(mylist)
    # part 2
    print "Let's delete the last item from your list. "
    mylist.pop(-1)
    print mylist
    removefruit = raw_input("What fruit would you like to remove?")
    longlist = mylist * 2
    print "Oh no the list multipled!\n" + str(longlist)
    badfruit(removefruit, longlist)
    print "Whew, that's better.\n" + str(longlist)
    # part3
    fixedlist = fixlist(mylist)
    print fixedlist
    # part4
    reverselist = reverselistitems(mylist)
    print reverselist
    mylist.pop(-1)
    reverselist = reverselistitems(mylist)
    print "Delete the last item of the original list."
    print "Original list & copy.\n" + str(mylist) + "\n" + str(reverselist)

mylist = makelist()
print mylist
runprogram(mylist)
