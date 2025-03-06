"""
 To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. 
 
 Neo reads the column from top to bottom and starts reading from the leftmost column.

 If there are symbols or spaces between two alphanumeric characters of the decoded script, 
 then Neo replaces them with a single space '' for better readability.

 Neo feels that there is no need to use 'if' conditions for decoding.

 Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

"""


#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Transpose the matrix to read column-wise
decoded_string = "".join("".join(column) for column in zip(*matrix))

# Replace non-alphanumeric characters between alphanumeric characters with a space
cleaned_string = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', decoded_string)

# Print the final decoded string
print(cleaned_string)
