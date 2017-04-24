"""
Dynamically Typed Hello World
"""

def hello(name):
    return 'Hello ' + name

print(hello('World')) 

"""
Statically Typed Hello World
"""

def hello(name: str) -> str: 
    return 'Hello ' + name

print(hello('World'))
print(hello(1)) #Type Check Error
