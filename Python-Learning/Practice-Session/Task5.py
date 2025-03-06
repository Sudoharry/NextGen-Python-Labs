## While loop (Indefinite Iteration)
## Use a while loop when you don't know in advance how many times the loop will run but want to continue executing as long as a condition is true

# Example: Keep asking for a password until it is correct.

password = ""

while password != "secure123":
    password = input("Enter password:")
print("Access granted")

## Use case: When the loop depends on a condition and should continue until the condition changes (e.g Waiting for user input, monitoring system status)