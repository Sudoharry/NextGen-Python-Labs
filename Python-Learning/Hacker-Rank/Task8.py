"""


"""

if __name__ == '__main__':
    n = int(input())  # Read the number of scores
    scores = list(map(int, input().split()))  # Convert input into a list of integers

    max_score = max(scores)  # Find the maximum score
    runner_up = max(x for x in scores if x != max_score)  # Find the second highest score

    print(runner_up)  # Print the runner-up score



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split()) # Read scores as a list of integers
    
    
#     max_score = max(arr)  # Find the maximum score
#     runner_up = max(x for x in arr if x != max_score)  # Find the second highest score
    
#     print(runner_up)  # Print the runner-up score
#     # print(sorted(set(scores))[-2])  


"""
Read n → The number of scores.
Read scores → Convert the input into a list of integers.
Find the maximum score → Using max(scores).
Find the second maximum (runner-up) → Use list comprehension to get the maximum of elements excluding the highest score.
Print the runner-up score.

"""

