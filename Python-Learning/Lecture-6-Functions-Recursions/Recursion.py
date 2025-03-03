## Recursion function

# def show(n):  #.. function name show
#     if (n == 0): #.. Base case decides whether the recursion should be stopped or not.
#         return #.. it will return control, doesn't control any value here.
#     print(n)
#     show(n-1)  #.. Show function is been infinitely call here, it's been stoped by n=0 
#     print("END")

# show(8)    


## call stack

# It will call function, in a stack. 


def fact(n):
    if(n == 0 or n == 1):
        return 1
    
    return fact(n-1) * n


print(fact(4))