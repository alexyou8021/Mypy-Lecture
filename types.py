from typing import Any

def a():
    return 1

def b() -> int:
    return 2

def c() -> float:
    return 2.5

def d() -> bool:
    return True

def e() -> str:
    return 'String'

def f() -> bytes:
    return b'x'

class obj:
    m = 3
    def __init__(self):
        self.n = 4

def g() -> object:
    return obj()

def h(o) -> Any:
    return o

print (a())
print (b())
print (c())
print (d())
print (e())
print (f())
print (g())

print (h(1))
print (h(2.5))
print (h('hello'))
print (h(True))
