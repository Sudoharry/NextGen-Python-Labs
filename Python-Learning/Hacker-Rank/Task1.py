
n = int(input().strip())

def check_num(n):
    if (n % 2 != 0):
       print("Weird")
    elif 2 <= n <= 5:
       print("Not Weird")
    elif 6 <= n <= 20:
       print("Weird")
    else:
       print("Not Weird")        
    
    
check_num(n)


# n = int(input().strip())

# if n % 2 == 1:  # Check if n is odd
#     print("Weird")
# elif 2 <= n <= 5:  # Check if n is even and in range 2 to 5
#     print("Not Weird")
# elif 6 <= n <= 20:  # Check if n is even and in range 6 to 20
#     print("Weird")
# else:  # If n is even and greater than 20
#     print("Not Weird")
