"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. 

The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

1 <=n <=10 power 5

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

"""

#!/bin/python3

import sys
from collections import OrderedDict

# Read input
n = int(sys.stdin.readline().strip())

word_count = OrderedDict()

# Process each word
for _ in range(n):
    word = sys.stdin.readline().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Output the number of distinct words
print(len(word_count))

# Output the occurrences in the order of appearance
print(" ".join(map(str, word_count.values())))


"""
Reading Input:

 The first line contains n, the number of words.
 The next n lines contain words.

Tracking Word Occurrences:

 We use an OrderedDict to store words as keys and their counts as values, ensuring order is maintained.

 Output:
  The number of distinct words (length of OrderedDict).
  The occurrences of each word in order of appearance.

 Complexity:
   O(n) time complexity (since we process each word once).
   O(n) space complexity (to store words in OrderedDict).


"""