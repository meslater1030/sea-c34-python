"""Question 1:
How can I use a list comprehension to generate
a mathmatical sequence?
"""


def cubes_by_four(num):
    cubes = [x**3 for x in range(num) if x**3 % 4 == 0]
    print cubes
cubes_by_four(50)
"""Question 2:
Can I use lambda to act as a filter for a list already
in existence?
"""

squares = [x**2 for x in range(1, 11)]


def between_30_and_70(lst):
    print filter(lambda x: x > 29 and x < 71, lst)
between_30_and_70(squares)

"""Question 3:
What does a a nested for loop look like when using a
list comprehension?
"""
suits = ["S", "H", "C", "D"]
faces = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def deck_of_cards(suits, faces):
    deck = [face + suit for suit in suits for face in faces]
    print deck
deck_of_cards(suits, faces)
