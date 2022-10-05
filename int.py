
a = 14.1

print(a)
print(f'hash {hash(a)}')
print(type(a))


print('-------------')


print(int(a))
print(f'hash {hash(int(a))}')
print(type(int(a)))

"""
The built-in round() function rounds values up and down.
The math.floor() function rounds down to the next full integer.
The math.ceil() function rounds up to the next full integer
"""

import math
print(math.ceil(2.01))
