# Print the sum of n numbers

"""
Input a number n, and return the sum of first n natural numbers.

Example: sum_n(5) --> 15 (1+2+3+4+5)

"""
# Using Formula
n = int(input("Enter the number:"))
# def sum_num(n):
#     return n * (n + 1) // 2

# sn = sum_num(n)
# print(sn)


# Using Loop method
def sum_num(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

sn = sum_num(n)
print(sn)