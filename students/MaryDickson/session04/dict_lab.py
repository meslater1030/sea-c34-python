mydict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print mydict
mydict.pop("cake")
print mydict
mydict["fruit"] = "mango"
print mydict
print mydict.keys()
print mydict.values()
print "cake" in mydict.keys()
print "mango" in mydict.values()

# using a dict constructor and zip build a dictionary of
# numbers from zero to fifteen
# and the hexadecimal equivalent (string is fine).


def hexnums():
    nums = range(0, 16)
    hexs = range(0, 10) + ["A", "B", "C", "D", "E", "F"]
    list = dict(zip(nums, hexs))
    return list

print hexnums()

newdict = mydict.copy()
print newdict


def changevals(dict):
    for k, v in dict.items():
        dict[k] = v.count("a")

print changevals(newdict)

