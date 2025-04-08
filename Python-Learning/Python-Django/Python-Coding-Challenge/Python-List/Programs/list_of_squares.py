"""
Write a function that returns a list of sequence of numbers from 1 to n
"""

def squares(n):
    return [i ** 2 for i in range(1, n + 1 )]

sq = squares(5)
print(sq)