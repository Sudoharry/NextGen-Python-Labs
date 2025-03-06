

""" You need to generate a list of all possible coordinates (i, j, k) for given values of x, y, and z, but exclude those where the sum i + j + k is equal to n. "
This should be done using list comprehensions."
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)


"""
1) Read Input: We take four integers x, y, z, and n from the input.

2) List Comprehension:
 - Iterate over i from 0 to x, j from 0 to y, and k from 0 to z.
 - Store the coordinates [i, j, k] in a list only if i + j + k != n.

3)Print the Result: The final list is displayed in lexicographically sorted order as required.

"""    


