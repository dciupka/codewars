print((lambda x: x)(1))
print((lambda x: x+1)(1))
print((lambda z: z+z)(1))
print((lambda x,y,z=1: x+y-z)(2,1))

# **kwargs in lambda
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print((lambda **keywordsargs: sum(keywordsargs.values()))(one=1, two=2,six=4))


# *args in lambda
print((lambda *args: sum(args))(1,2,3))


print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))

def add_1(x):
    return (lambda x:x+1)(x)

print(add_1(20))

