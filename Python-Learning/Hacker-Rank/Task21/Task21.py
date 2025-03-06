from itertools import combinations

def probability_of_a(N, letters, K):
    # Get the indices where 'a' appears
    indices = [i for i, letter in enumerate(letters) if letter == 'a']

    # Generate all possible selections of K indices
    total_combinations = list(combinations(range(N), K))
    favorable_combinations = [comb for comb in total_combinations if any(i in indices for i in comb)]

    # Calculate probability
    probability = len(favorable_combinations) / len(total_combinations)
    
    # Print probability rounded to 3 decimal places
    print(f"{probability:.3f}")

# Input handling
if __name__ == "__main__":
    N = int(input().strip())  # Read N
    letters = input().strip().split()  # Read list of N letters
    K = int(input().strip())  # Read K

    probability_of_a(N, letters, K)



"""
Find Indices of 'a'

Identify the positions where 'a' occurs in the list.
Generate All Possible Combinations of K Selections

Use itertools.combinations to generate all ways to pick K indices.
Count Favorable Outcomes

Count how many selections include at least one 'a'.
Compute Probability

Divide the count of favorable outcomes by the total combinations.
Output Result

Print the probability rounded to three decimal places.

"""
