## Print the second elements of the list

# def find_the_second_largest_element(nums):
#     unique_nums = list(set(nums)) # This would remove the duplicate values

#     if len(unique_nums) < 2: # If the elements are less than 2 then it will return None
#         return None
#     unique_nums.sort(reverse=True) # Unique numbers will  be sorted first and then it will be in reverse order
#     return unique_nums[1] # This would print the index[1] which means second element

# print(find_the_second_largest_element([102,50,50,80,99,99,100,101]))

## Find duplicating elements

def find_non_repeating_char(character):
    seen = set()
    duplicates = set()

    for char in character:
        if char in seen:
            duplicates.add(char)
        seen.add(char)
    return list(duplicates)       

print(find_non_repeating_char("aabbccddeelkj"))
          





