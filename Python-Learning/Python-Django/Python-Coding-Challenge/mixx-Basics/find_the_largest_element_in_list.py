""" Finding a prime number we need to understand what should be the logic, 

    1) A prime number should be sqrt(n)
    2) A number less than 2 is not a prime number
    3) Any number which is divisible by 1 and own is prime number.   
"""

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(3))