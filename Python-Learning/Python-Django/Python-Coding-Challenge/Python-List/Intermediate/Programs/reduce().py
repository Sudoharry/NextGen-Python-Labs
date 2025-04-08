# Using reduce() for Aggregation (from functools


from functools import reduce

numbers = [1,2,3,4,5]

# Sum of all elements

total = reduce(lambda x,y: x * y, numbers)
print(total)


"""
  1) from funtools import reduce

   - This imports the reduce function from Python's functools module
   - reduce() is used to apply a function cumulatively to elements in an iterable, reducing them to a single value
   
   2) reduce(lambda x,y: x + y, numbers)
    
    -  A function(lambda x, y: x +  y)
    - An iterable ( numbers = [1,2,3,4,5])




"""