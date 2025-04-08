## Transposing a Matrix (List of Lists)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose using list comprehension
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transposed)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
