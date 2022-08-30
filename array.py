a = [1, 5.2, 4, 0, -1]
def sum_array(a):
    z=0
    for i in a:
       z+=i
    return z

print(sum_array(a))

def sum_array(a):
  return sum(a)


def sum_array(a):
    return sum(a) if a else 0

'''
import codewars_test as test
from solution import sum_array

@test.describe("Testing sum array")
def tests():
    @test.it("Fixed tests")
    def fixed_tests(): 
        test.assert_equals(sum_array([]), 0)
        test.assert_equals(sum_array([1, 2, 3]), 6)
        test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
        test.assert_equals(sum_array([4, 5, 6]), 15)
        test.assert_equals(sum_array(range(101)), 5050)
  

'''