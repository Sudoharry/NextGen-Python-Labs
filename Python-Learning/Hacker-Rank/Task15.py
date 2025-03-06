"""


"""

#!/bin/python3

import itertools

# Read input
K, M = map(int, input().split())

lists = []
for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])  # Exclude the first number, as it represents the count of elements

# Generate all possible combinations of elements, one from each list
max_value = 0
for combination in itertools.product(*lists):
    S = sum(x**2 for x in combination) % M
    max_value = max(max_value, S)

# Print the maximum possible value
print(max_value)



"""
Input Handling:
 Read the integers K (number of lists) and M (modulo divisor).
 Read the K lists, ignoring the first integer of each line (as it represents the count of elements).
 Generating Combinations:
 Use itertools.product(*lists) to generate all possible combinations, picking one element from each list.
 Computing Maximum S Value:
 For each combination, calculate the sum of squares modulo M.
 Track the maximum value encountered.
 Complexity:
 Since K ≤ 7, brute force using itertools.product() is feasible.

"""