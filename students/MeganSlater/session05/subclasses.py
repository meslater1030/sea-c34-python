# Four Questions

"""Question 1:
Can I replace a method that has been inherited from another class?
"""


class Superclass(object):
    def super_method(self):
        print("I'm the method of the super class")
    name = "Super"


class Subclass(Superclass):
    def super_method(self):
        print("I'm the method of the sub class")
    pizza = "peperroni"
super_class = Superclass()
sub_class = Subclass()
super_class.super_method()
sub_class.super_method()

"""Question 2:
Can a subclass inherit from more than one super class?
"""
"""
class Inbred(Superclass, Subclass):
    def __init__(self):
        print(self.pizza + self.name)
this generates an error. Python cannot decide which super_method to use
not to mention that you wouldn't want to inherit a superclass and its
subclass.  It would make more sense to make another subclass.
"""


class Other_Superclass(object):
    pizza = "Cheese"


class Inbred_Two(Superclass, Other_Superclass):
    def __init__(self):
        print(Superclass.name + Other_Superclass.pizza)
inbred_class = Inbred_Two()

"""Question 3:
Can a method in a subclass alter a method in a superclass without
replacing it entirely?
"""


class Extender(Superclass):
    def super_method(self):
        Superclass.super_method(self)
        print("I'm an extension of the super method")
Extender = Extender()
Extender.super_method()

"""Question 4:
If I change an attribute in a superclass after that superclass has already
been initialized does it populate out to all the subclasses?
"""
Superclass.name = "Bob"
print(Subclass.name)
print(Inbred_Two.name)
print(Extender.name)
