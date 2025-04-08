
# Write a function to compute the factorial of a number using recursion.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial())