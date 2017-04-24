from typing import Any

def one():
    return 1

def two() -> int:
    return 2

def three() -> None: #Does not expect return value
    return 3

def four() -> str: #Expects string; Returns integer
    return 4

def five() -> Any:
    return 5


a = one()
print(a)

b= two()
print(b)

c = three()
print(c) #Type Check Error

d = four()
print(d) #Type Check Error

e = five()
print(e) 
assert isinstance(e, int)
