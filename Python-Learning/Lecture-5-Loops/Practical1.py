# Q1 Print number from 1 to 100

# i= 1

# while i <= 100:
#     print("Hello", i)
#     i += 1

# print("Loop Ended")    


# Q2 Print numbers from 100 to 1


# i= 100

# while i >= 1:   ## stopping condition
#     print("Hello", i)
#     i -= 1

# print("Loop Ended")    


# Q3 Print the multiplication on number n.

# i = 1
# n = int(input("Enter the multiplication table number:"))

# while i<=10:
#     print(n*i)
#     i += 1

# print("Loop ended")

# Q4 Print the elements of the following list using a loop 

# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3]) #... print(num[len(nums)-1])



# nums = [1,4,9,16,25,36,49,64,81,100] 
# heroes = ["Superman", "Ironman", "Thor", "Hanuman", "Hulk"] #.. traverse kar means or travel karna ek ek index pe
# idx = 0

# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1

# while idx < len(nums):
#     print(nums[idx]) #.. nums[0], nums[1], nums[2], nums[3]...
#     idx += 1


# nums = (1,4,9,16,25,36,49,64,81,100,36)

# x = 36
# i = 0 # intialization

# while i < len(nums):
#     if (nums[i] == x):
#       print("Found at idx", i) 
#       break 
#     else:
#        print("Finding...", i)  
#     i += 1
# print("End of the loop")


# i = 1

# while i <= 10:
#     print(i)

#     if(i == 7 ):
#         break
#     i += 1

# print("End of the loop")


i = 0

while i <= 10:
    if(i%2 != 0):
        i += 1
        continue ## continue acts as skip
    print(i)
    i += 1
