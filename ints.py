def one():
    return 1

def two() -> int:
    return 2

def three() -> None:
    return 3

def four() -> str: #Expects string; Returns integer
    return 4


a = one()
print(one())

b= two()
print(two())

c = three()
print(three()) #Type Check Error

d = four()
print(four()) #Type Check Error
