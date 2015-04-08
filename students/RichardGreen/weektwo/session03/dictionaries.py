# dictionary
test_scores = {'Ethan Hawke': 78, 'Charles Bronson': 85, 'Gene Simmons': 59,
'Paul Walker': 87}

# sets
a = set([1, 2, 3, 10, 15, 4, 5, 6, 9, 8, 7])

b = set([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4])

c = '15'

'''In this module we create a dictionary of test scores. This has names and
their scores. Outlined below we create two functions that can operate off this
dictionary'''


def name_lookup(x, y):
    '''function definition: enter a name and lookup a score
arguments: a dictionary'''
    print "Your user: ' %s ' has a score of:" % (y)
    print x[y]


def highest_score(x):
    '''function definition: provide me the name and
value for the highest score arguments: a dictionary'''
    print "The highest score belongs to:"
    print max(x, key=x.get)


def add_to_set(x, y):
    '''function definition: add values to a pre-existing set.
    arguments: a value x and a set y'''
    print "The updated set is:"
    y.update(x)
    print y


def summary_set_stats(x, y):
    '''function definition: provide summary statistics off two sets, this
includes: the union, intersection , and difference between the sets.
'''
    print " the union of the two sets are:"
    print x.union(y)

    print " the values that intersect the two sets are:"
    print x.intersection(y)

    print " the differences between the two sets are:"
    print x.difference(y)


if __name__ == "__main__":
    name_lookup(test_scores, 'Ethan Hawke')
    highest_score(test_scores)
    add_to_set(c, a)
    summary_set_stats(a, b)
