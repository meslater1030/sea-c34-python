# Three questions from session 3 slides on iterations


def createindex(string):
    index = []
    for idx, letter in enumerate(string):
        index = index + (idx, letter)
    return index
print "This is a test for createindex:"
print createindex('I am a string')
print createindex('Stringystring')
