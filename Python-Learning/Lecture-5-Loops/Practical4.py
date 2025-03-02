#... WAP to find the sum of first n number (using while)
#.. sum= 1+2+3+4+5

# n = 5
# sum = 0 
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# # for i in range(1, n+1):
# #     sum += i

# print("Total sum=", sum)

#.. WAP to find the factorial of first n numbers(using for)


n = 5
fact = 1   #.. we initialize the variable everytime with 1.
i = 1
for i in range(1, n+1):
    fact *= i
    i += 1

print("factorial=", fact)   