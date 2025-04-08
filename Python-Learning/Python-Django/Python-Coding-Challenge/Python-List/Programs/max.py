""" Find Max in a List
    Write a function that returns the largest 
    number in a given list without using max(). 
"""


# Method1: Using the reverse function or sorted function

def find_max(lst):
    if not lst:
        raise ValueError("List is not defined")
    
    max_num = lst[0]

    for num in lst[1:]:
        if num > max_num:
            max_num = num
    return max_num

fmax = find_max([2,3,5,6,7,8])
print(fmax)