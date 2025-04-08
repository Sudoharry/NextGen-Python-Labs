# Count occurences, sorting, reverse sorting, index of a element, check if element exits, length of list

nums = [11,22,33,44,55,66,22,77,88,99,111,12,31,54]

# Count occurences
print(nums.count(22)) # This will check the nums element and search in the list of element 22 and count the occurences and then print

# Sorting the list which is already exists into a proper format in ascending order
nums.sort() # Solve the sorting errors fail to add the parenthesis after the sort in built function
print(nums)

# Reverse sorting 
nums.sort(reverse=True)
print(nums)

# Length of element
print(len(nums))


# # Check if the element exists
print(45 in nums) # Within the print function we have check the specific numbers we want to see if it exists


# Index of an element
print(nums.index(33))

