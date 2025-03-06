from collections import Counter

def most_common_chars(s):
    # Count occurrences of each character
    char_count = Counter(s)

    # Sort by occurrence count (descending), then by character (ascending)
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the top 3 most common characters
    for char, count in sorted_chars[:3]:
        print(char, count)

# Example usage:
if __name__ == "__main__":
    s = input().strip()  # Read input string
    most_common_chars(s)


"""
1) Count occurrences

Counter(s) generates a dictionary where keys are characters and values are their counts.

2)Sorting logic

Primary sorting: Descending order of occurrences (-x[1] ensures higher counts appear first).
Secondary sorting: If counts are the same, sort alphabetically (x[0]).

3)Print top 3 characters

Using sorted_chars[:3], we extract and print the top 3.

"""