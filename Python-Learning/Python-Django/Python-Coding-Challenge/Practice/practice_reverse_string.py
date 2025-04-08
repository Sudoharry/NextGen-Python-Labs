# 1) Slicing 


# def reverse_srting(s):
#     return s[::-1]

# print(reverse_srting("Hello"))

# 2) reveresed()

# def reverse_string(s):
#     return "".join(reversed(s))


# print(reverse_string("Hello"))


# 3) Concatenation method which is inefficient way of doing it, but we will try

def reverse_string(s):
    result = ''

    for char in s:
        result = char + result
    return result

print(reverse_string("Hello"))

"""
   Inefficient way of doing it the reason is as it consumes a lot of memory. As for example if the string
   is 10,000 character long in that case, it might use a lot of memory as when we use + (concatenation)
   what happens is everytime a new string is created which due to nature of python list which is immutable.
"""

# 4) Best approach and efficient way of doing it using list  as a stack

def reverse_string(s):
    stack = list(s)
    result = ''

    while stack:
        result += stack.pop()
    return result

print(reverse_string("Hello")) 


