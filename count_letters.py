"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""
def count(string):
    res={}
    for chr in string:
        if chr in res:
            res[chr]+=1
        else:
            res[chr]=1
    return res



#other
from collections import Counter

def count(string):
    return Counter(string)

#cool

def count(string):
    return {i: string.count(i) for i in string}