## The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.


if __name__ == '__main__':
    n = int(input("Enter number from 1 to 5:"))
    for i in range(n):
        print(i ** 2)
      


"""
1) Reading Input: n = int(input()) reads an integer from standard input.

2) Looping Through Integers: for i in range(n): iterates over all non-negative integers less than n, starting from 0 up to n-1.

3) Printing Squares: print(i ** 2) calculates the square of i and prints it.
"""
