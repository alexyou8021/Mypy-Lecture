"""
Dynamically Typed Fibonacci Function
"""

def inc(n):
    x = n
    for i in range(0,x):
        yield i

nums = inc(5) #Dynamically Typed  Variable
for num in nums:
    print(num)

"""
Statically Typed Fibonacci Function
"""

from typing import Iterator #imports specific types

def s_inc(n: int) -> Iterator[int]: #n must be int; output must be Iterator[int]
    x = n
    for i in range(0,x):
        yield i

nums = s_inc(5) #Statically typed variable
for num in nums:
    print(num)
