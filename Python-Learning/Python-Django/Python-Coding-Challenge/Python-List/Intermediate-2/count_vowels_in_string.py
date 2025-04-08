# def  count_vowels(s):
#     vowels= "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)

# print(count_vowels("Hello world"))



"""
    Count the vowels using a loop (in one line)

    What's happening here? 
        return sum(1 for char in s if char in vowels)

        - We go through each letter (char) in s one by one
        - If letter is in the vowels list , we count it (1)
        - We add up all these 1s using the sum()

"""

# Alternative without using the list comprehension:

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0 # Start with 0 vowels

    for char in s:  # Loop through each letter
        if char in vowels:  # If it's  a vowel
            count += 1 # Increase the count
    return count

print(count_vowels("Harry"))