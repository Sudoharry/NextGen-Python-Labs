#  Find the Second Largest Element in a List


def second_largest(nums):
    unique_num = list(set(nums))  # Remove duplicates numbers
    if len(unique_num) < 2: # If there are less than 2 numbers, return None
        return None
    unique_num.sort(reverse=True) # Sort the unique number in descending number
    return unique_num[1] # Return the second element with second largest

print(second_largest([10, 12, 15, 16, 17])) 



""" 
Code Breakdown:

- The set(nums) removes duplicates values from the list
- The list() function converts the set back into a list

## Sort the list in descending order

unique_number.sort(reverse=True)

- The .sort(reverse=True) function sort the list in the descending order(largest to smallest)
- 

"""