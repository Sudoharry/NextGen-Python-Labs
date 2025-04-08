# Removing the duplicates from a list


nums = [10,20,30,20,10,40,50]


# Using sets
# unique_nums = list(set(nums))   # Using the set will remove the duplicates here
# print(unique_nums)

# Maintaining orders
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)


"""
        1) Initialize the empty list unique_nums = []
        2) Iterate through nums
        3) for num in nums
            - For num in nums will be checked before adding it to unique_nums
        4) Check if number is already in the uniquq_nums:

                    - if nums not in unique_nums:
                        (This ensures that only the first occurences of each number is added)
        5) The not in condition ensures that duplicates are removed while preserving order.

"""