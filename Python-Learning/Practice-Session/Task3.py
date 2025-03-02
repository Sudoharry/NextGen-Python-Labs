"""
  Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

  write a program that prints out all the elements of the list that are less than 5.

"""

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# # for val in a:
# #     if (val < 5):
# #       print(val) 

# print( [ val for val in a if val < 5 ] ) ##  Writing this in one line of code


## Extra: Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
lessNnums =[]

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
num =int(input("Enter the number:"))

for n in numbers:
    if n < num:  
        lessNnums.append(n) #.. Add numbers that are less than user name to our list.
        lessNnums.sort() #.. sort list

# Print the list    
print(lessNnums)    


