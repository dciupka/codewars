"""Mutable Definition

Mutable is when something is changeable or has the ability to change.
In Python, ‘mutable’ is the ability of objects to change their values.
These are often the objects that store a collection of data."""

"""
Objects of built-in type that are mutable are:
    Lists
    Sets
    Dictionaries
    User-Defined Classes (It purely depends upon the user to define the characteristics) 
"""
# mutable is unhashable
list_1 = ['dawid', 'mariola']
list_2 = ['dawid', 'mariola']
list_3 = ['mariola', 'dawid']
print(list_2 == list_1)  # True
print(list_2 == list_3)  # False


set_1 = {'dawid', 32, 'mariola', 31}
set_2 = {32, 'mariola', 31, 'dawid'}
print(set_1 == set_2)  # True


dic_1 = {'dawid': 32, 'mariola': 31}
dic_2 = {'dawid': 32, 'mariola': 31}
print(dic_1 == dic_2)  # True
dic_3 = {'mariola': 31, 'dawid': 32}
print(dic_1 == dic_3)  # True
