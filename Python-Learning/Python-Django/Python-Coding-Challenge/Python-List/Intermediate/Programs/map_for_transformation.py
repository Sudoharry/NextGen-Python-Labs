## Filtering a List Using List Comprehension

 # map() applies a function to each element in the list.


numbers = [1,2,3,4,5]

# Square each numbers

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

"""
1) numbers = [1, 2, 3, 4, 5]

 - This is a list of numbers.

2) map(lambda x: x ** 2, numbers)

 - map(function, iterable) applies a function to each element of an iterable (like a list).

Here, the function is a lambda function: lambda x: x ** 2, which takes x and returns x squared.

 - The map() function returns a map object, so we use list() to convert it into a list.

3) Lambda Function (lambda x: x ** 2)

 - lambda x: x ** 2 is a small anonymous function that takes x and returns x^2.

 - It does the same thing as:"


 Summary:
  - map() applies a function (lambda x: x ** 2 ) to reach element in numbers 
  - lambda is short, anonymous function 
  - list(map(...)) converts the results into a list
  - Equivalent to a for loop but more concise.

"""