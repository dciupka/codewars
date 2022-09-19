"""
Implement the function unique_in_order which
 takes as argument a sequence and returns a list of items without any elements
 with the same value next to each other and preserving the original order of elements.
"""


def unique_in_order(iterable):
    new = []
    for i in iterable:
        if not new:
            new.append(i)
        elif new[-1] != i:
            new.append(i)
    return new


unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1, 2, 2, 3, 3])
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])

from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

#unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]