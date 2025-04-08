# Find duplicate numbers

# def find_duplicate(nums):

def duplicate_num(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

print(duplicate_num([1,2,3,4,1,2]))


# Find non repeating character

from collections import Counter

def find_non_repeating_char(s):
    count = Counter(s)

    for char in s:
        if count[char] == 1:
            return char
    return None

print(find_non_repeating_char("aabbccddefe"))


# Reverse the string

def reverse_string(s):
    return " ".join((s.split()[::-1]))

print(reverse_string("Hello Django Developer"))
