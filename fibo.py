#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13,

def fibo(length):
    fibos = []
    for i in range(length):
        if i <=1:
            fibos.append(i)
        else:
            fibos.append(fibos[-1]+fibos[len(fibos)-2])
    return fibos

print(fibo(10))
print(fibo(10)[-3])

def fibs():
    return 'better code'









def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1



def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
