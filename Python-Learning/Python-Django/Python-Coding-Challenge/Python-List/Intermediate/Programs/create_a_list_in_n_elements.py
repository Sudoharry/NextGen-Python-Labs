""" 
Create a list with n elements

Problem: Write a python program to create a list of n elements entered by a user.

Hint: Use input or append"
 
"""

n = int(input("Enter the numbers of elements:"))

list = [input(f"Enter element {i + 1 }:") for i in range(n)]

print("Your list", list)


