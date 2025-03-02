## How to use the set in the python

# Set are unique and immutable, means we cannot change the set values or we cannot add duplicate values in the set.

# collection = {1,2,2,2,3,4, "Harry", "Barot", "Harry", "Barot"} # The duplicate values in the set is ignored, and doesn'throws any error.

# print(collection.pop())
# print(collection.intersection())

# print(type(collection))
# print(len(collection))



## Set Methods

# set.add(el)

# 

# collection = set() # empty set; syntax
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add("Harry")
# collection.add((1,2,3))
# # collection.remove(2)

# collection.clear()
# print(len(collection))
# # print(collection)

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))