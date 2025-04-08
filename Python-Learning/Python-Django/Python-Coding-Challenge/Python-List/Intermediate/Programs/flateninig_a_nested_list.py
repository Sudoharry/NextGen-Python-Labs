nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# Flatten list using list comprehension
flat_list = [item for sublists in nested_list for item in sublists]
print(flat_list)


# Alternative way to Flatten a Nested List:
 

"""
   > nested_list: is a list of lists

   - It contains a sublist: [[1,2,3],[4,5],[6,7,8]]
   - We want to flatten this nested structure into a single list

   > This is a nested list comprehension, equivalent to:

    - flat_lists = []
    for sublists in nested_list: # Loop through each sublist
        for item in sublists: # Loop through each element inside the sublist
         flat_lists.append(items)

    > Key Concepts: 

    - Outer Loop(for sublist in nested_list) 
        - Iterates through each sublists in nested_list

    - Inner Loop(for items in sublists)
        - Iterates through each elements inside the current sublist

    - Final result:
       - Combines all individual elements into a single list
                        
"""

"""
   1)  Using sum()

    flat_list = sum(nested_list,[])
    print(flat_list)

    > sum(nested_list, []) adds all sublists together into a single list.

    2) Using itertools.chain()

    from itertools import chain
    flat_lists = list(chain(*nested_list))
    print(flat_lists)

    > chain(*nested_list) flattens multiple lists into one.
""" 

