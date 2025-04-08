"""
Write a function to compute the factorial of n numbers
"""
# Method:1 Using the for loop method
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

fact = factorial(5)
print(fact)

# Method:2  Using the recursion method
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(5)
print(fact)

# Method:3 Using the math.factorial in-built method
import math

def factorial(n):
    return math.factorial(n)

fact = factorial(5)
print(fact)
