"""Your task is to make a function that can take any non-negative
 integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number."""

#first option

def descending_order(num):
    nums = [x for x in str(num)]
    nums.sort(reverse=True)
    new = ''
    for char in range(len(nums)):
        new += nums[char]
    return int(new)

descending_order(123456789)

'''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')

'''