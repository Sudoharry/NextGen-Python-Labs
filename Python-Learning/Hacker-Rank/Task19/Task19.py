


def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):  # Split s into n/k substrings of size k
        substring = string[i:i+k]
        seen = set()
        unique_substring = ""
        for char in substring:
            if char not in seen:
                unique_substring += char
                seen.add(char)
        print(unique_substring)  # Print each result on a new line

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
Splitting the string

The input string s is divided into equal-sized substrings of length k.
Since k is a factor of n, s is evenly divisible.
Removing duplicate occurrences

A set (seen) is used to track unique characters in each substring.
Only the first occurrence of a character is kept in the order it appears.
Printing results

Each processed substring (uᵢ) is printed on a new line.

"""    