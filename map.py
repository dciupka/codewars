def calculateSquare(n):
    return n*n

numbers=(1,2,3,4,45)

result = set(map(calculateSquare, numbers))
print(result)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)

print(list(result))