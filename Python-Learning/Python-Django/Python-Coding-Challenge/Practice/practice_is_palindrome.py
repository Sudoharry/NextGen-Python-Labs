
## Write a function that checks whether a given string is a palindrome (reads the same forward and backward).

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("RACECAR"))
# print(is_palindrome("DDDADA"))



# Stack based approch using the efficient way
# Instead of using [::-1], we can use a stack (LIFO - Last In, First Out).

def is_palindrome(s):
    stack = list(s)   # Convert string to list (acting as a stack)
    reverse_d = ''

    while stack:
        reverse_d += stack.pop()  # Pop last element and append to new string
    return s == reverse_d  # Compare original with reversed

print(is_palindrome("RACECAR"))
