# Function to perform an arithmetic operations
# Create an calculator which can perform addition, difference, product and division

def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2


# Checking if second number is zero to avoid division by zero
    if num2 != 0:
     division_result = num1 / num2

    else:
      print("Division by zero is not allowed")

    return sum_result, difference_result, product_result, division_result


## User input

num1 =  float(input("Enter the first number:"))
num2 =  float(input("Enter the second number:"))


## Perform the operations

sum_result, difference_result, product_result, division_result = arithmetic_operations(num1, num2)


# Display the results

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")

