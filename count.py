array = [1, 0, 1, 2, 0, 1, 3]
print([x for x in array if x] + [0] * array.count(1))  # if x because 0 ==False
print(array.count(0))
print([0, 1] * 10)
print(False == 0)
