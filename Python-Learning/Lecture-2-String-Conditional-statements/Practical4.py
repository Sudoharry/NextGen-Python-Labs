# WAP to find the greatest of 3 numbers entered by the users

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))


# if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):  # num1 is greater than num2 and num1 is greater than num3 then num1 is greatest
#     print("First number is the greatest:", num1)

# elif(num2 >= num1) and (num2 >= num3) and (num2 >= num4): # num2 is greater than num1 and num1 is greater than num3 then num1 is greatest
#     print("Second number is the greatest:", num2)

# elif(num3 >= num1) and (num3 >= num2) and (num3 >= num4): # num2 is greater than num1 and num1 is greater than num3 then num1 is greatest
#     print("Third number is the greatest:", num3)   
    
# else:
#     print("Fourth number is the greatest:", num4)

print("The greatest number is:", max(num1, num2, num3, num4))  ## We can do it using max() function if we don't need to use if conditional statement.