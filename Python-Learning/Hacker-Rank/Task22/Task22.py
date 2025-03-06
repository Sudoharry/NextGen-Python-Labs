def custom_sort(s):
    # Separate characters into different categories
    lower = sorted([c for c in s if c.islower()])
    upper = sorted([c for c in s if c.isupper()])
    odd_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 1])
    even_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

    # Concatenate results in the required order
    sorted_string = ''.join(lower + upper + odd_digits + even_digits)
    
    return sorted_string

# Read input
s = input().strip()
print(custom_sort(s))


"""
Categorize characters:
Extract lowercase letters, uppercase letters, odd digits, and even digits separately.
Sort each category individually.
Concatenate them in the required order:
Lowercase letters → Uppercase letters → Odd digits → Even digits.
Return the final sorted string.
"""