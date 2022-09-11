'''
Immutable Definition

Immutable is the when no change is possible over time.
In Python, if the value of an object cannot be changed over time, then it is known as immutable.
Once created, the value of these objects is permanent.
'''

'''
Objects of built-in type that are immutable are:

    Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
    Strings
    Tuples
    Frozen Sets
    User-Defined Classes (It purely depends upon the user to define the characteristics)
'''

# Proof
number = 1
print(hash(number))
new_number = 1
print(hash(new_number))

name = 'dawid'
print(hash(name))
new_name = 'dawid'
print(hash(new_name))

tuple_1 = ('dawid', 'mariola')
print(hash(tuple_1))
tuple_2 = ('dawid', 'mariola')
print(hash(tuple_2))
tuple_3 = ('mariola', 'dawid')
print(hash(tuple_3)) # no the same tuple
print(tuple_3==tuple_2)

