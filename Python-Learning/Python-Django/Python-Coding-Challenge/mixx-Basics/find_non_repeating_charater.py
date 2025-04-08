## Concepts Used: Hashing (Counter from collections)

from collections import Counter

def first_non_repeating_character(s):
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating_character("aabbcde"))    



"""
Code Breakdown:

1) from collections import Counter

- Counter is a built-in Python class from collection module
- It helps count the frequency of elements in a collection(like a string, list or tuple)

Ex: Counter("aabbcde")  
# Output: Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1})


2) count = Counter(s)

- Counter(s) creates a dictionary like object where:
     - Keys are character
     - Values are the number of times each character appears.

- Example:      
        s = "aabbcde"
        count = Counter(s)
        print(count)  # Output: {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1}

3) for char in s:

- We iterate over the original string s, checking each character in order.

4) if count[char] == 1:
    return char

    - The count[char] gives the frequency of char in s.
    If a character appears only once (== 1), it is the first non-repeating character.
    Example Execution:
    "a" appears 2 times → skip.
    "b" appears 2 times → skip.
    "c" appears 1 time → return "c".

5) If No unique characters exits 

        - Return None

- if all characters repeat,return None

6) Step-by-Step Execution for "aabbcde"

Character	Frequency	Action
a	            2	    Skip
b	            2	    Skip
c	            1	    ✅ Return "c"


"""