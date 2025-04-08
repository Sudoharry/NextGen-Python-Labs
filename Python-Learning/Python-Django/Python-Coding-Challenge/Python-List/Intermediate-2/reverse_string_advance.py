# Write a Python function to reverse a string without using [::-1] or reversed().

"""
    Instead of using string concatenation (which is inefficient due to new string creation each time), 
    a more stack-friendly approach is to use Python’s built-in list (acting as a stack):
"""

# Alternative approach using a stack (Most efficient approach of reversing the string)

def reverse_string_stack(s):
    stack = list(s)  # Convert string to list (acting as stack)
    result = ''
    
    while stack:
        result += stack.pop()  # Pop last character and append to result
    
    return result

print(reverse_string_stack("hello"))  # Output: "olleh"


""" 
    Inefficient way of concentating the string as it creates new string each time.
    
    In Python, srings are immutable, meaning they cannot be modified in place, Everytime you concatenate,
    strings using +, Python creates  a new string instead of modifying the existing one
"""

def reverse_string(s):
    result = ''

    for char in s:
        result =  char + result
    return result

print(reverse_string("Hello"))


""" 
    Explaination: 

    Understand Step by step execution to understadnd what's happening when we use the string concatenation
    method.

    Example "Hello"
    Step -> 1   char-'h'  -----> New string h is created
    Step -> 2   char-'eh' -----> New string eh is created
    Step -> 3   char-'leh' -----> New string leh is created
    Step -> 4   char-'lleh' -----> New string lleh is created
    Step -> 5   char-'olleh' -----> New string olleh is created

    --> How python allocated memory?

    ~ Each time result = char + result
       - Python doesn't modify result
       - It creates new string & assigns reference to the result
       - The old string becomes garbage and waits for python's garbage collector

    Conclusion: This happens because strings in python are immutable, and Python cannot modify them in place.
    
"""