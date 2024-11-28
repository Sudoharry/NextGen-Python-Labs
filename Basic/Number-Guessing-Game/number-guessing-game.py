# A simple number guessing game
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess the number (between 1 and 10):")
guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {secret_number}.")
