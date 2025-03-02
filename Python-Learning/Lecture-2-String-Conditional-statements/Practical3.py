# WAP to check the number entered by the user is odd or even.

num = int(input("Enter the number to check if it's odd or even:"))

if (num % 2) == 0:
    num1 = "EVEN"
else:    
    num1 = "ODD"

print ("The provided number is:", num1)