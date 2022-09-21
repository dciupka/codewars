"""Write an algorithm that takes an array and moves all of the zeros to the end,
 preserving the order of the other elements.
 move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
 """


def move_zeros(lst):
    without_zero = [i for i in lst if i != 0]
    zero = [i for i in lst if i == 0]
    return without_zero + zero


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    without_zero = [i for i in lst if i != 0]
    zero = [i for i in lst if i == 0]
    for i in lst:
        if i != 0:
            without_zero.append(i)
        else:
            zero.append(0)
    lst = without_zero + zero
    return lst

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)

def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)



"""
import codewars_test as test
from solution import move_zeros

@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])

"""