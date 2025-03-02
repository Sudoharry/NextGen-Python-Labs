""" 
 Task:

 Create a program that asks the user to enter their name and their age. 
 Print out a message addressed to them that tells them the year that they will turn 100 years old. 

 Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
 If you want to do this in a generic way, see exercise 39.

"""

name = input("Enter the name:")
age = int(input("Enter the age:"))

future_age = 2024 - age + 100
print(name, "you'll be 100 years old on", str(future_age))


#.. So, using the age we can calculate the future age, using the current year - age + 100 formula, so this way we can calculate the age of an student.
