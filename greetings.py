def greet(name):
    return f'Hello, {name} how are you doing today?'


def greet(name):
    return "Hello, %s how are you doing today?" % name

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

greet = lambda name: f'Hello, {name} how are you doing today?'