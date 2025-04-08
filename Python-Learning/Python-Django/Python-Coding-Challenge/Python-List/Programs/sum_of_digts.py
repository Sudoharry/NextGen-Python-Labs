"""
    Problem 5: Sum of Digits
    Write a function sum_digits(n) that returns the sum of all digits in an integer n.  
"""

def sum_digit(n):
    total = 0

    for digit in str(abs(n)):
            total += int(digit)
    return total

sd = sum_digit(123)
print(sd)
                      