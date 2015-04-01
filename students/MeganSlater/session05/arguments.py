"""Question 1:
How can  I use arguments from a tuple in multiple places
in my function?  So argument 1 is in one place, argument
two is in another etc.  Do I have to know how many things
are in the tuple to begin with?
"""

"""
Commented out because it throws an error.
def mismatch(args):
    spam, plus, eggs, other = args
    print("I'd like to eat " + spam + " " + plus + " " + eggs + ".")

newtuple = ("Spam", "and", "Eggs")
print mismatch(newtuple)
"""
"""mismatch uses values from the tuple but the tuple will only unpack
correctly if we assign the same number of variables as the length of
the tuple.  It runs correctly if 'other' is deleted but throws an error as is.
"""
"""Question 2:
How can I use arguments from a dictionary in multiple places in my
function?  Do I have to know how many entries are in the dictionary in
order to use it properly?
"""


def dictunpack(kwargs):
    print("No one expects the {place[0]} {action[0]}!".format(**kwargs))
    print("No one expects the {place[1]} {action[1]}!".format(**kwargs))

dict = {"place": ["Spanish", "Boston"], "action": ["Inquisition", "tea party"]}
dictunpack(dict)

"""It seems like you probably need to know how the information in your
dictionary is formatted and what's there if you're going to use kwargs.
Or else there's some way to iterate through the dictionary that
I haven't figured out yet.
"""

"""Question 3:
Why might I want to make a shallow copy instead of a deep copy of a
list or dictionary?
"""


bears = {"Team": "Da Bears", "Field Conditions": ["dry", "sunny"]}
seahawks = bears.copy()
seahawks["Team"] = "Seahawks"


def updateconditions():
    bears["Field Conditions"].append('windy')
updateconditions()
print(bears, seahawks)
"""In this case if the Bears and the Seahawks are playing each other
we might want to update the dictionaries to include various things
about each team but the playing conditions would be the same for both.
"""
