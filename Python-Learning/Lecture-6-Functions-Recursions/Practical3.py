#.. WAF to find the factorial of n. (n is the parameter)

n = int(input("Enter the number to find the factorial:"))

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(n)