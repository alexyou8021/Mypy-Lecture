"""
Dynamically Typed Fibonacci Function
"""

from typing import Iterator #imports specific types

def inc(n: int) -> Iterator[int]: #n must be int; output must be Iterator[int]
    x = n
    for i in range(0,x):
        yield i

nums = inc(5) #Statically typed variable
for num in nums:
    print(num)
