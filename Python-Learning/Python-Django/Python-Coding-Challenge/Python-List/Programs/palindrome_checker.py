"""🔢 Problem 2: Palindrome Checker
    Write a function is_palindrome(word) that returns True 
    if the string is a palindrome (same forwards and backwards), 
    and False otherwise.
"""

def palindrome_checker(s):
    if s == s[::-1]:
        return True
    else:
        return False

pc =  palindrome_checker("KAKA")
print(pc)

# If the word is case-sensitive
# def is_palindrome(word):
#     word = word.lower()  # Make it case-insensitive
#     return word == word[::-1]

# isp = is_palindrome("RACECAR")
# print(isp)

