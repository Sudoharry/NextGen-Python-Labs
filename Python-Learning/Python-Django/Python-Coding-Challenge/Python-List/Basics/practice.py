
"""This is practice exercise where I will learn about inserting and deleting the element from the list"""

numbers = [55,12,16,4,48,15,22,11]

# Add the number in the list, will use the append() which will add the element in the list.
# numbers.append(100)

# Add the element at index[4] in the list in the already existing list
# numbers.insert(4,40)


# Merge the list with already existing list that we have in the numbers variables.
numbers.extend([100,101])

numbers.pop(4)
# del numbers[9]

print(numbers)


