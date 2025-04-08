# Find common elments between two lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8] 

# Using List comprehension

common = [num for num in list1 if num in list2]
print(common)

# Using set intersection

# common = list(set(list1) & set(list2))
# print(common)