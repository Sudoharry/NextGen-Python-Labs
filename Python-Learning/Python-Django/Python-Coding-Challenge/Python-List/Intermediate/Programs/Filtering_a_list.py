# Filtering a List Using List Comprehension


numbers = [15,5,57,66,99,33,44,22]

# Get numbers divisible by 3
filtered_number = [num for num in numbers if num % 11 == 0]
print(filtered_number)
