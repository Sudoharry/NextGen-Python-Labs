
"""  Create a program which prints the number from 1 to 50 
    Condition1: From 1 to 50, if number is divisible by 3 print "Fizz"
    Condition2: From 1 to 50, if number is divisible by 5 print "Fizz" 
    Condition3: If number is divisible by 3 and 5 both then print "FizzBuzz"
 """

for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
        
