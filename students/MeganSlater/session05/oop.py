# Two questions

# Question 1:
# what is something in the standard library that's object oriented?
a_string = "My name is Megan."
# a string is an object that has attributes and methods
print(a_string.count('a'))  # string has a built in method of count
print(len(a_string))  # string has a built in function of length


class Mammal(object):
    """How can use of object oriented programming help make programs
    more readable?
    """
    characteristics = {
     "blood": "warm blooded",
     "lays eggs": False,
     "live birth": True,
     "vertebrate": True,
    }


class Cat(Mammal):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    Mammal.characteristics["sound"] = "Meow"
    Mammal.characteristics["legs"] = 4

Evie = Cat("Evie", "black")
print("%s is a %s cat and has the following characteristics: "
      % (Evie.name, Evie.color))
print(Evie.characteristics)

