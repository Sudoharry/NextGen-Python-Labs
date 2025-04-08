## Finding the Most Frequent Element

from collections import Counter

nums = [1, 2, 3, 1, 2, 1, 4, 5, 1, 2]

most_common = Counter(nums).most_common(1)
print(most_common)  # [(1, 4)]
