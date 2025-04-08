# Removing the elements from the list

numbers = [10,20,30,40,50]

# Remove by value
numbers.remove(20) # This will remove the value from the list by searching whole list

# Remove by index
del numbers[0] # This will remove the first element of the list that we have as we have mentioned the 0 index.

#Pop (removes the last element by default)
numbers.pop()  # This will remove the last element of the list which is 50 here in this case.

# This will remove specific index that we have mentioned in this case we have mentioned 2 index[2] will be removed from the list
numbers.pop(2)

print(numbers)


