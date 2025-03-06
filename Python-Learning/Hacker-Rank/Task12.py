"""
 There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
 You like all the integers in set A and dislike all the integers in set B. 
 Your initial happiness is 0. For each i integer in the array, if i E A, you add 1 to your happiness. 
 If i E B, you add -1 to your happiness. Otherwise, your happiness does not change. 
 Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
"""


def calculate_happiness():
    # Read input values
    n, m = map(int, input().split())  # Read n and m
    array = list(map(int, input().split()))  # Read the array of n elements
    A = set(map(int, input().split()))  # Read set A (liked numbers)
    B = set(map(int, input().split()))  # Read set B (disliked numbers)
    
    # Compute happiness score
    happiness = sum((i in A) - (i in B) for i in array)
    
    # Print final happiness
    print(happiness)

# Execute the function
if __name__ == '__main__':
    calculate_happiness()
