# Write a recursive function to print all elements in a list.
# Hint: Use list & index as parameter.


fruits = ["Mangoes", "Banana", "Apple", "Cheery", "Chickoo", "Rasberyy", "Papaya"]
   
def print_list(list, idx=0): #.. Function takes a list and an index (default=1)
    if (idx == len(list)):  #.. Base case: Stop when idx reaches the length of the list
        return
    print(list[idx])    #.. Print the current element
    print_list(list, idx + 1)   #.. Recursive call with the next index

print_list(fruits)      #.. Call function with fruits list


## reverse function

def print_list_reverse(list, idx=None):
    if idx == None:
        idx = len(list)-1
    
    if idx < 0:
        return

    print(list[idx])
    print_list_reverse(list, idx - 1)

print_list_reverse(fruits)        


# for fruit in reversed(fruits):
#     print(fruit)


# for fruit in fruits[::-1]:  # List slicing to reverse
#     print(fruit)