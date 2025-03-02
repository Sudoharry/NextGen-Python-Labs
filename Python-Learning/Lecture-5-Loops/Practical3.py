## Using for and range()
# Print numbers for 1 to 100

# for i in range(1,101):
#     print(i)


# Print numbers from 100  to 1

# for i in range(100,0, -1):  ## har bar decrease by 1
#     print(i)



# Print the multiplication table of number n.
n = int(input("Enter the number for multiplication table:"))

for i in range(1,11):
    print(n * i)