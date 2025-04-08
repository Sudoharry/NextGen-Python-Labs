
# Find duplicate elements in a List

def find_elements(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    return list(duplicates)

print(find_elements([1,2,3,4,2,3,5]))


# from collections import Counter

# def find_duplicates(nums):
#     count = Counter(nums)
#     return [num for num, freq in count.items() if freq > 1]

# print(find_duplicates([1, 2, 3, 4, 2, 3, 5]))

"""
Code Breakdown

1) def find_duplicates(nums)
 - Defines a function find_duplicates(nums), where nums is a list of numbers
 - The goal is to find & return a list of duplicates from nums

2) Initializing Two Sets]
- seen = set()
      - seen:  Keeps tracks of numbers we have already encountered   
- duplicates = set()
      - duplicates: Stores numbers than repeat more than once.

3) Checking For Duplicates
    - if num in seen:
        duplicates.add(num)

            - If the numbers already exits in seen,it means we found a duplicate
            - Add it to duplicate

4) Adding numbers to seen

-  seen.add(num)
   - if the numbers isn't in seen, we add it into seen for future check


5) Return the duplicates

 -return list(duplicates)
     - Converts the duplicate set into a list and return it

Iteration Breakdown
Iteration	num	    seen Before	duplicates Before 	Action
1st	        1	        {}	            {}	       Add 1 to seen
2nd	        2	        {1}	            {}	       Add 2 to seen
3rd	        3	        {1, 2}	        {}	       Add 3 to seen
4th	        4	        {1, 2, 3}	    {}	       Add 4 to seen
5th	        2	        {1, 2, 3, 4}	{}	       Duplicate! Add 2 to duplicates
6th	        3	        {1, 2, 3, 4}	{2}	       Duplicate! Add 3 to duplicates
7th	        5	        {1, 2, 3, 4}	{2, 3}	    Add 5 to seen     


Alternative method:

from collections import Counter

def find_duplicates(nums):
    count = Counter(nums)
    return [num for num, freq in count.items() if freq > 1]

print(find_duplicates([1, 2, 3, 4, 2, 3, 5]))
# Output: [2, 3]

"""
