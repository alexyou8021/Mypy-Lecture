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

