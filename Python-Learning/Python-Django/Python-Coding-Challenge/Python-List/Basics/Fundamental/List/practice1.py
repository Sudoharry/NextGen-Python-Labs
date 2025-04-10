"""
    Create a list of your favorite movies and print each.

    Sort and reverse a list of numbers.

    Remove duplicates from a list using a set.
"""

# Task 1:
# movies = ['DDLJ', 'Sholay', 'Gravity', 'Inception', 'MSD-The untold story']

# for movie in movies:
#     print(movie)


# Task 2:

numbers = [5,3,6,9,7,2,1,0,1]

# Sort the numbers
numbers.sort()
print(f'Sorted numbers: {numbers}')

# Reverse the numbers
numbers.sort(reverse=True)

print(f'Reverse list: {numbers}')
rm_duplicates = set(numbers)
print(f'Unique numbers: {rm_duplicates}')

# Remove the duplicates numbers
