import random

# Character sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><["

# Combine all characters
all_chars = lower + upper + numbers + symbols

# Ask user for desired password length
length = int(input("Enter a length: "))

# Generate password using random.sample to ensure unique characters
password = ''.join(random.sample(all_chars, length))

# Display the password
print("Generated Password:", password)
