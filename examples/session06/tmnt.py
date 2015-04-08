class Turtle(object):

    def __init__(self, name):
        """Initialize a turtle."""
        self.name = name

    def announce(self):
        """Print out an introduction."""
        print("{name} says hello.".format(self.name))


class TMNT(Turtle):

    def __init__(self, name, color, weapon):
        """Initialize a teenage mutant ninja turtle with properties."""
        self.name = name
        self.color = color
        self.weapon = weapon

    def announce(self):
        """Print out an introduction."""
        intro = "{name} wears {color} and has a {weapon}"
        print(intro.format(
            name=self.name,
            color=self.color,
            weapon=self.weapon
        ))

if (__name__ == "__main__"):
    t1 = TMNT("Leonardo", "blue", "katana")
    t2 = TMNT("Raphael", "red", "sai")
    t3 = TMNT("Donatello", "purple", "bo staff")
    t4 = TMNT("Michelangelo", "orange", "nun-chuks")
    t5 = Turtle("World Turtle")
    turtles = [t1, t2, t3, t4, t5]
    for t in turtles:
        t.announce()
