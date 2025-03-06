""" 
 Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,$ .
Both players have to make substrings using the letters of the string $.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string $ .

For Example:
String $ = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:"


Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string $.
Note: The string $ will contain only uppercase letters: [A-Z].

"""


def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        points = length - i  # Substrings starting from index i
        if string[i] in vowels:
            kevin_score += points
        else:
            stuart_score += points

    # Printing the result as per the required format
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Example usage
if __name__ == "__main__":
    s = input().strip()  # Read input string
    minion_game(s)


"""
Instead of generating substrings explicitly (which is inefficient), we count how many times each letter can be the start of a substring.
The number of substrings that start at index i is len(string) - i (since it extends to the end).
If the starting character is a vowel, Kevin gets the points.
If the starting character is a consonant, Stuart gets the points.
Finally, we compare their scores and declare the winner.

"""