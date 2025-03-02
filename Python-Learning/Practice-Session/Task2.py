"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Hint: how does an even / odd number react differently when divided by 2?

"""

n = int(input("Enter the number & I will tell you whether it's odd or even:"))

if (n % 2) == 0:
    print("Provided number is even")
else:
    print("Number is odd")


# Extra : If the number is a multiple of 4, print out a different message.

n = int(input("Enter the number:"))

if (n % 4) == 0:
    print(n , "number is multiple of 4")
else:
    print(n, "number is not multiple of 4")

# Extra
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Give me a number to check:"))
check = int(input("Give me a number to divide by:"))

if (num % check) == 0:
    print(num,"divides evenly by", check)

else:
        print(num,"does not divides evenly by", check) 
    
        