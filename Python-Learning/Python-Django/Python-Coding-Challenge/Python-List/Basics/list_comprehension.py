# List comprehsion

# squares = [x ** 3 for x in range(1,9)]
# print(squares)


# even numbers

# even_numbers = [x for x in range(2,100) if x % 2 == 0]
# print(even_numbers)

""" expression for items in iterable if condition

    1) expression: What you want to put in the list(here, x)
    2) for items in iterable: The loop (here, x in range (2,100))
    3) if condition -> A filter here (x % 2 == 0)


    In others words, x before for in the iterable for loops which is expression,
    This is the value that gets added to the list. Since we just write x, it means "add x " as it is"


"""


even_numbers = []

for i in range(2,101):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)        