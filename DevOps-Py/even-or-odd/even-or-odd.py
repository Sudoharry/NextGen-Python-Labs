# Function to check the numberis odd or even

def check_even_odd(number):
     if number % 2 == 0:
         return "Even"
     else:
         return "Odd"


# Input from users
num=int(input("Enter the number"))

# Determine the number is odd or even
result =  check_even_odd(num)

# Output
print(f"The number {num} is {result}")

