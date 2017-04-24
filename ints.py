def one():
    return 1

def two() -> int:
    return 2

def three() -> None:
    return 3


a = one()
print(one())

b= two()
print(two())

c = three()
print(three()) #Type Check Error
