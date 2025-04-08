"""
    Find the Second Largest Number in a List (Intermediate)
    Write a function to find the second-largest number in a list without using max() more than once.

"""

def second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            first, second = num, first
        elif second < num < first:
            second = num
    return second

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45



"""
    Find Duplicate Elements in a List (Intermediate)
    Write a function that returns a list of duplicate elements.
"""


def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 2, 3, 5, 6, 3]))  # Output: [2, 3]



"""
    Check If a Number is Prime (Intermediate)
    Write a function that checks if a number is prime.

"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10)) # False


"""
    Find Missing Number in a List (Intermediate)
    Given a list of n unique numbers from 1 to n+1, find the missing number.    

"""

def find_missing(lst):
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(lst)

print(find_missing([1, 2, 3, 5]))  # Output: 4


"""
    Anagram Checker (Intermediate)
    Write a function to check if two strings are anagrams of each other

"""

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False



"""
    Generate a Random Password (Intermediate)
    Write a function to generate a random password with a mix of letters, numbers, and symbols.

"""

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password(12))  # Output: A random 12-character password


"""
    Find the Longest Word in a Sentence (Intermediate)
    Write a function to return the longest word in a given sentence.

"""

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("The quick brown fox jumped over the lazy dog"))  # Output: "jumped"


"""
    Find the Intersection of Two Lists (Intermediate)
    Write a function to return the common elements between two lists.

"""

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]



"""
    Find All Permutations of a String (Advanced)
    Write a function to return all possible permutations of a string.

"""

from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(string_permutations("abc"))
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


"""
    Implement a Simple Calculator (Intermediate)
    Write a function that takes two numbers and an operator (+, -, *, /) and performs the operation.

"""

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '/'))  # Output: 2.0


"""

 Try to practice this programs on your own
 
"""





