""" 
    Find the Second Largest Number in a List
    Write a function second_largest(nums) that returns the second-largest number from a list.

    Ex: 
    second_largest([4,7,2,9,5])
"""

# DIY

"""
1) sorted_list using the sorted in built function
2) reverse_list variables which will reverse the list using the slicing method
3) return the list[1] which will be the second largest number in the list
"""
# def second_largest_no(num):
#     sorted_list = sorted(num)
#     reverse_list =  sorted_list[::-1]
#     return reverse_list[1]

# sln = second_largest_no([88,100,50,8,66,99,77,5,66,46,23])
# print(sln)


"""
    Efficient way
"""

def second_largest(nums):
    unique_nums = list(set(nums))  # Remove the duplicates values

    if len(unique_nums) < 2:   # For debugging if num is less than 1
        return None
    
    second = largest = float('-inf')

    for num in unique_nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    return second

sec_lar = second_largest([10,20,30,40,50,60,20,30,70])
print(sec_lar)







""" 
    Real Life Analogy
    Imagine you're at a race:

You’re trying to figure out who’s 1st and who’s 2nd fastest.
As each runner finishes:
If someone is faster than your 1st, they take 1st and the old 1st drops to 2nd.
If they’re slower than 1st but faster than 2nd, they take 2nd.
   
"""

