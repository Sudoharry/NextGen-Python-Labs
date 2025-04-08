""" Problem 4: Count Vowels in a String
    Write a function count_vowels(s) that returns the number of vowels 
    (a, e, i, o, u) in the string s 
"""


def count_vowels(s):
    vowels = ("AEIOUaeiou")

    count = 0

    for char in s:
        if char in vowels:
            count += 1
    return count

cov = count_vowels("AI is cool")
print(cov)
        