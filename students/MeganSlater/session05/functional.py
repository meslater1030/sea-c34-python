"""Question 1:
What's a simple way to sum a list
within a dictionary?
"""
d = {"donations": [2, 5, 9, 20]}


def sumlist(lst):
    summed = reduce(lambda x, y: x + y, lst)
    print summed
sumlist(d["donations"])

"""Question 2:
Can I use a filter on a dictionary?
"""

d = {"Megan": "friend", "Ben": "enemy", "David": "friend"}


def rid_m_names(dict):
    enemies = filter(lambda x: x[0] != "M", dict.keys())
    print enemies
rid_m_names(d)

"""So the answer to this is yes but I'm unclear on whether
it's terribly useful to create a new filtered list of either keys or values
from a dictionary.  I'd rather create a new, filtered dictionary"""

"""Question 3:
Can I use maps to help determine the effect of inflation
on items from a dictionary?
"""
basket = {"Apples": 0.40, "Bottled Water": 1.2, "Gas": 3.98}


def inflation(i):
    print map(lambda x: x * i, basket.values())
inflation(1.02)
"""ibid above.  This function might be useful if you
were trying to reduce it to calculate the total cost
of the basket depending on a certain amount of inflation
but I still think it woudl be more useful to be able
to create a new dictionary that showed the effects of inflation.
"""
