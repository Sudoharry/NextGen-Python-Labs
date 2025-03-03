#.. WAF to print the elements of the list in a single line (list is the parameter)

cities= ["Mumbai","Gujarat","Delhi","Bihar","Chennai","Madhya Pradesh","Banglore","Tamil Nadu","Assam"]
heroes = ["Hanuman", "Angad", "Jamvan", "Akshay Kumar", "Bahubali", "Ravan", "Indrajit", "Vibhishan"]

# print(heroes[0], end="")
# print(heroes[1], end="")

def print_list(list):
    for items in list:
        print(items, end=" ")


print_list(cities)
print()