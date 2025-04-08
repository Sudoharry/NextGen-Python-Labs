
## Sorting a List with a Custom Key   # PENDING

students = [("Alice", 25), ("Bob", 22), ("Charlie", 24)]

# Sort by age (2nd element)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  
# [('Bob', 22), ('Charlie', 24), ('Alice', 25)]
