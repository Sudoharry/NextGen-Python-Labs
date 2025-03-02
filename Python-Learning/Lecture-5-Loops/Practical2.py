## Print the elements of the following list using a loop:

# element = [1,4,9,16,25,36,49,64,81,100]

# for el in element:
#     print(el)

# else:
#     print("End of the loop")       


## Search for a number x  in this tuple using the loop

nums = [1,4,9,16,25,36,49,64,81,100,49]

x = 49
idx = 0

for el in nums:
    if (el == x):   ## linear search
     print("Number found at idx", idx)
    idx += 1